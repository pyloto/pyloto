"""
O.T.T.O Assistant Service
Integrates the existing OpenAI assistant configuration with the new system
"""
import json
from typing import Dict, Any, Optional
import logging
from datetime import datetime

from ..core.config import settings
from ..core import cache
from ..models.user import User
from ..models.order import Order, OrderStatus
from ...packages.integrations.openai import OpenAIClient, OTTOAssistant
from ...packages.integrations.whatsapp import WhatsAppClient

logger = logging.getLogger(__name__)


class OTTOService:
    """
    O.T.T.O (Operador de Tráfego e Tecnologia de Operações) Service
    Handles all AI assistant interactions for delivery orchestration
    """
    
    def __init__(self):
        self.openai_client = OpenAIClient(
            api_key=settings.OPENAI_API_KEY,
            assistant_id=settings.OPENAI_ASSISTANT_ID
        )
        self.otto_assistant = OTTOAssistant(self.openai_client)
        
        if settings.WHATSAPP_API_TOKEN:
            self.whatsapp_client = WhatsAppClient(
                api_url=settings.WHATSAPP_API_URL,
                token=settings.WHATSAPP_API_TOKEN,
                phone_number_id=settings.WHATSAPP_PHONE_NUMBER_ID
            )
        else:
            self.whatsapp_client = None
    
    async def start_conversation(self, user_phone: str, user_id: Optional[str] = None) -> str:
        """Start a new conversation with O.T.T.O"""
        try:
            # Create or get existing thread
            cache_key = f"otto:thread:{user_phone}"
            thread_id = await cache.get(cache_key)
            
            if not thread_id:
                thread_id = await self.otto_assistant.start_conversation(user_id)
                # Cache thread for 24 hours
                await cache.set(cache_key, thread_id, expire=24 * 60 * 60)
            
            logger.info(f"Started O.T.T.O conversation for {user_phone}, thread: {thread_id}")
            return thread_id
            
        except Exception as e:
            logger.error(f"Error starting O.T.T.O conversation: {e}")
            raise
    
    async def process_whatsapp_message(
        self,
        phone_number: str,
        message_text: str,
        message_id: str,
        user: Optional[User] = None
    ) -> Dict[str, Any]:
        """Process incoming WhatsApp message through O.T.T.O"""
        try:
            # Get or create conversation thread
            thread_id = await self.start_conversation(phone_number, user.id if user else None)
            
            # Prepare order context if user has active orders
            order_context = None
            if user:
                order_context = await self._get_user_order_context(user.id)
            
            # Send message to O.T.T.O
            response = await self.otto_assistant.send_message(
                thread_id=thread_id,
                message=message_text,
                user_id=user.id if user else None,
                order_context=order_context
            )
            
            # Parse O.T.T.O response (should be JSON)
            try:
                otto_response = json.loads(response)
            except json.JSONDecodeError:
                # Fallback to text response
                otto_response = {
                    "kind": "chat",
                    "text": response
                }
            
            # Handle different response types
            result = await self._handle_otto_response(otto_response, phone_number, user)
            
            # Mark WhatsApp message as read
            if self.whatsapp_client:
                await self.whatsapp_client.mark_as_read(message_id)
            
            return result
            
        except Exception as e:
            logger.error(f"Error processing WhatsApp message: {e}")
            return {
                "success": False,
                "error": str(e),
                "response_text": "Desculpe, ocorreu um erro. Tente novamente em alguns minutos."
            }
    
    async def _handle_otto_response(
        self,
        otto_response: Dict[str, Any],
        phone_number: str,
        user: Optional[User] = None
    ) -> Dict[str, Any]:
        """Handle different types of O.T.T.O responses"""
        try:
            response_kind = otto_response.get("kind", "chat")
            
            if response_kind == "question":
                # O.T.T.O is asking for more information
                return await self._handle_question_response(otto_response, phone_number)
            
            elif response_kind == "quote":
                # O.T.T.O generated a delivery quote
                return await self._handle_quote_response(otto_response, phone_number, user)
            
            elif response_kind == "fsm_event":
                # O.T.T.O wants to trigger a state machine event
                return await self._handle_fsm_event(otto_response, phone_number, user)
            
            else:  # "chat" or unknown
                # Regular chat response
                return await self._handle_chat_response(otto_response, phone_number)
                
        except Exception as e:
            logger.error(f"Error handling O.T.T.O response: {e}")
            return {
                "success": False,
                "error": str(e)
            }
    
    async def _handle_question_response(
        self,
        otto_response: Dict[str, Any],
        phone_number: str
    ) -> Dict[str, Any]:
        """Handle O.T.T.O question responses"""
        try:
            text = otto_response.get("text", "Preciso de mais informações.")
            
            # Send text message via WhatsApp
            if self.whatsapp_client:
                await self.whatsapp_client.send_text_message(phone_number, text)
            
            return {
                "success": True,
                "type": "question",
                "response_text": text,
                "requires": otto_response.get("requires", [])
            }
            
        except Exception as e:
            logger.error(f"Error handling question response: {e}")
            return {"success": False, "error": str(e)}
    
    async def _handle_quote_response(
        self,
        otto_response: Dict[str, Any],
        phone_number: str,
        user: Optional[User] = None
    ) -> Dict[str, Any]:
        """Handle O.T.T.O quote responses"""
        try:
            text = otto_response.get("text", "Cotação gerada")
            quote_data = otto_response.get("metadata", {}).get("quote", {})
            
            # Create interactive message with confirmation buttons
            if self.whatsapp_client:
                buttons = [
                    {"id": "confirm_order", "title": "✅ Confirmar"},
                    {"id": "modify_order", "title": "✏️ Modificar"},
                    {"id": "cancel_order", "title": "❌ Cancelar"}
                ]
                
                await self.whatsapp_client.send_interactive_message(
                    to=phone_number,
                    body_text=text,
                    buttons=buttons,
                    header_text="💰 Cotação de Entrega"
                )
            
            # Store quote in cache for later confirmation
            cache_key = f"otto:quote:{phone_number}"
            await cache.set(cache_key, otto_response, expire=30 * 60)  # 30 minutes
            
            return {
                "success": True,
                "type": "quote",
                "response_text": text,
                "quote_data": quote_data
            }
            
        except Exception as e:
            logger.error(f"Error handling quote response: {e}")
            return {"success": False, "error": str(e)}
    
    async def _handle_fsm_event(
        self,
        otto_response: Dict[str, Any],
        phone_number: str,
        user: Optional[User] = None
    ) -> Dict[str, Any]:
        """Handle FSM state change events"""
        try:
            event = otto_response.get("fsm_event")
            text = otto_response.get("text", "Estado atualizado")
            
            # Here you would integrate with your FSM system
            # For now, just send confirmation
            
            if self.whatsapp_client:
                await self.whatsapp_client.send_text_message(phone_number, text)
            
            return {
                "success": True,
                "type": "fsm_event",
                "event": event,
                "response_text": text
            }
            
        except Exception as e:
            logger.error(f"Error handling FSM event: {e}")
            return {"success": False, "error": str(e)}
    
    async def _handle_chat_response(
        self,
        otto_response: Dict[str, Any],
        phone_number: str
    ) -> Dict[str, Any]:
        """Handle regular chat responses"""
        try:
            text = otto_response.get("text", "Como posso ajudar?")
            
            if self.whatsapp_client:
                await self.whatsapp_client.send_text_message(phone_number, text)
            
            return {
                "success": True,
                "type": "chat",
                "response_text": text
            }
            
        except Exception as e:
            logger.error(f"Error handling chat response: {e}")
            return {"success": False, "error": str(e)}
    
    async def _get_user_order_context(self, user_id: str) -> Optional[Dict[str, Any]]:
        """Get user's current order context for O.T.T.O"""
        try:
            # This would query your database for active orders
            # For now, return None
            return None
            
        except Exception as e:
            logger.error(f"Error getting user order context: {e}")
            return None
    
    async def handle_button_interaction(
        self,
        phone_number: str,
        button_id: str,
        user: Optional[User] = None
    ) -> Dict[str, Any]:
        """Handle WhatsApp button interactions"""
        try:
            if button_id == "confirm_order":
                return await self._confirm_order(phone_number, user)
            elif button_id == "modify_order":
                return await self._modify_order(phone_number, user)
            elif button_id == "cancel_order":
                return await self._cancel_order(phone_number, user)
            else:
                return {
                    "success": False,
                    "error": f"Unknown button: {button_id}"
                }
                
        except Exception as e:
            logger.error(f"Error handling button interaction: {e}")
            return {"success": False, "error": str(e)}
    
    async def _confirm_order(self, phone_number: str, user: Optional[User] = None) -> Dict[str, Any]:
        """Confirm order and generate payment"""
        try:
            # Get cached quote
            cache_key = f"otto:quote:{phone_number}"
            quote_data = await cache.get(cache_key)
            
            if not quote_data:
                if self.whatsapp_client:
                    await self.whatsapp_client.send_text_message(
                        phone_number,
                        "❌ Cotação expirada. Por favor, solicite uma nova cotação."
                    )
                return {"success": False, "error": "Quote expired"}
            
            # Generate PIX payment through O.T.T.O
            thread_id = await self.start_conversation(phone_number, user.id if user else None)
            
            payment_message = "Confirmo o pedido. Por favor, gere o PIX para pagamento."
            response = await self.otto_assistant.send_message(
                thread_id=thread_id,
                message=payment_message,
                user_id=user.id if user else None
            )
            
            # Parse and handle payment response
            try:
                payment_response = json.loads(response)
                return await self._handle_otto_response(payment_response, phone_number, user)
            except json.JSONDecodeError:
                if self.whatsapp_client:
                    await self.whatsapp_client.send_text_message(phone_number, response)
                return {"success": True, "response_text": response}
                
        except Exception as e:
            logger.error(f"Error confirming order: {e}")
            return {"success": False, "error": str(e)}
    
    async def _modify_order(self, phone_number: str, user: Optional[User] = None) -> Dict[str, Any]:
        """Allow user to modify order"""
        try:
            message = "O que você gostaria de modificar no pedido?"
            
            if self.whatsapp_client:
                await self.whatsapp_client.send_text_message(phone_number, message)
            
            return {"success": True, "response_text": message}
            
        except Exception as e:
            logger.error(f"Error modifying order: {e}")
            return {"success": False, "error": str(e)}
    
    async def _cancel_order(self, phone_number: str, user: Optional[User] = None) -> Dict[str, Any]:
        """Cancel current order"""
        try:
            # Clear cached quote
            cache_key = f"otto:quote:{phone_number}"
            await cache.delete(cache_key)
            
            message = "❌ Pedido cancelado. Posso ajudar com algo mais?"
            
            if self.whatsapp_client:
                await self.whatsapp_client.send_text_message(phone_number, message)
            
            return {"success": True, "response_text": message}
            
        except Exception as e:
            logger.error(f"Error canceling order: {e}")
            return {"success": False, "error": str(e)}