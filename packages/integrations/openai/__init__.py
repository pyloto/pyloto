"""
OpenAI Integration Package
Handles all OpenAI API interactions including the O.T.T.O assistant
"""
import openai
from typing import Optional, Dict, Any, List
import json
import logging
from datetime import datetime

logger = logging.getLogger(__name__)


class OpenAIClient:
    """OpenAI API client wrapper"""
    
    def __init__(self, api_key: str, assistant_id: str = "asst_RGAVvFf5IhLa8tShJ0gZWsYX"):
        self.client = openai.OpenAI(api_key=api_key)
        self.assistant_id = assistant_id
        
    async def create_thread(self) -> str:
        """Create a new conversation thread"""
        try:
            thread = self.client.beta.threads.create()
            return thread.id
        except Exception as e:
            logger.error(f"Error creating OpenAI thread: {e}")
            raise
    
    async def send_message(
        self,
        thread_id: str,
        message: str,
        user_id: Optional[str] = None,
        metadata: Optional[Dict[str, Any]] = None
    ) -> str:
        """Send a message to the assistant"""
        try:
            # Add message to thread
            self.client.beta.threads.messages.create(
                thread_id=thread_id,
                role="user",
                content=message,
                metadata=metadata or {}
            )
            
            # Run the assistant
            run = self.client.beta.threads.runs.create(
                thread_id=thread_id,
                assistant_id=self.assistant_id
            )
            
            # Wait for completion and get response
            while run.status in ["queued", "in_progress", "requires_action"]:
                # Handle function calls if needed
                if run.status == "requires_action":
                    run = await self._handle_function_calls(run, thread_id)
                else:
                    run = self.client.beta.threads.runs.retrieve(
                        thread_id=thread_id,
                        run_id=run.id
                    )
            
            if run.status == "completed":
                # Get the latest assistant message
                messages = self.client.beta.threads.messages.list(
                    thread_id=thread_id,
                    order="desc",
                    limit=1
                )
                
                if messages.data:
                    content = messages.data[0].content[0]
                    if hasattr(content, 'text'):
                        return content.text.value
                    
            logger.error(f"Assistant run failed with status: {run.status}")
            return "Desculpe, ocorreu um erro ao processar sua mensagem."
            
        except Exception as e:
            logger.error(f"Error sending message to OpenAI: {e}")
            raise
    
    async def _handle_function_calls(self, run, thread_id: str):
        """Handle function calls from the assistant"""
        try:
            tool_outputs = []
            
            for tool_call in run.required_action.submit_tool_outputs.tool_calls:
                function_name = tool_call.function.name
                function_args = json.loads(tool_call.function.arguments)
                
                # Handle different function calls
                output = await self._execute_function(function_name, function_args)
                
                tool_outputs.append({
                    "tool_call_id": tool_call.id,
                    "output": json.dumps(output)
                })
            
            # Submit tool outputs
            run = self.client.beta.threads.runs.submit_tool_outputs(
                thread_id=thread_id,
                run_id=run.id,
                tool_outputs=tool_outputs
            )
            
            return run
            
        except Exception as e:
            logger.error(f"Error handling function calls: {e}")
            raise
    
    async def _execute_function(self, function_name: str, args: Dict[str, Any]) -> Dict[str, Any]:
        """Execute a function call from the assistant"""
        try:
            if function_name == "compute_delivery_quote":
                return await self._compute_delivery_quote(args)
            elif function_name == "search_faq":
                return await self._search_faq(args)
            elif function_name == "get_driver_eta":
                return await self._get_driver_eta(args)
            elif function_name == "summarize_order":
                return await self._summarize_order(args)
            elif function_name == "generate_pix_payment":
                return await self._generate_pix_payment(args)
            else:
                logger.warning(f"Unknown function call: {function_name}")
                return {"error": f"Unknown function: {function_name}"}
                
        except Exception as e:
            logger.error(f"Error executing function {function_name}: {e}")
            return {"error": str(e)}
    
    async def _compute_delivery_quote(self, args: Dict[str, Any]) -> Dict[str, Any]:
        """Compute delivery quote with Google Maps integration"""
        try:
            # Import here to avoid circular imports
            from ..google import GoogleMapsClient
            from ...core.config import settings
            
            maps_client = GoogleMapsClient(settings.GOOGLE_MAPS_API_KEY)
            
            # Calculate route if addresses provided
            if "origin_address" in args and "dest_address" in args:
                route_info = await maps_client.get_route_info(
                    args["origin_address"],
                    args["dest_address"]
                )
                
                return {
                    "distance_km": route_info.get("distance_km"),
                    "eta_min": route_info.get("duration_minutes"),
                    "traffic_level": route_info.get("traffic_level", "normal"),
                    "time_of_day": self._get_time_of_day(),
                    "zone_key": "curitiba.urbana",  # Default zone
                    "weather": "normal",  # TODO: Integrate weather API
                }
            else:
                # Return provided values or defaults
                return {
                    "distance_km": args.get("distance_km", 10.0),
                    "eta_min": args.get("eta_min", 30),
                    "traffic_level": "normal",
                    "time_of_day": self._get_time_of_day(),
                    "zone_key": "curitiba.urbana",
                    "weather": args.get("weather", "normal"),
                }
                
        except Exception as e:
            logger.error(f"Error computing delivery quote: {e}")
            return {"error": str(e)}
    
    async def _search_faq(self, args: Dict[str, Any]) -> Dict[str, Any]:
        """Search FAQ information"""
        # TODO: Implement FAQ search
        return {
            "content": "FAQ content would be returned here based on the query.",
            "query": args.get("query", "")
        }
    
    async def _get_driver_eta(self, args: Dict[str, Any]) -> Dict[str, Any]:
        """Get driver ETA to pickup location"""
        try:
            from ..google import GoogleMapsClient
            from ...core.config import settings
            
            maps_client = GoogleMapsClient(settings.GOOGLE_MAPS_API_KEY)
            
            # Calculate ETA from driver to pickup
            driver_location = f"{args['driver_lat']},{args['driver_lng']}"
            pickup_location = args.get("pickup_address", f"{args.get('pickup_lat')},{args.get('pickup_lng')}")
            
            if pickup_location:
                route_info = await maps_client.get_route_info(driver_location, pickup_location)
                return {
                    "eta_minutes": route_info.get("duration_minutes", 15),
                    "distance_km": route_info.get("distance_km", 5.0)
                }
            else:
                return {"eta_minutes": 15, "distance_km": 5.0}
                
        except Exception as e:
            logger.error(f"Error getting driver ETA: {e}")
            return {"eta_minutes": 15, "distance_km": 5.0}
    
    async def _summarize_order(self, args: Dict[str, Any]) -> Dict[str, Any]:
        """Generate order summary with markup"""
        try:
            base_amount = args.get("amount", 0)
            markup_rate = args.get("markup_rate", 0.10)  # 10% default markup
            final_amount = base_amount * (1 + markup_rate)
            
            summary_text = f"""
📦 **Resumo do Pedido**

📍 **Coleta:** {args.get('origin_formatted', 'N/A')}
🎯 **Entrega:** {args.get('dest_formatted', 'N/A')}

👤 **Remetente:** {args.get('remetente_nome', 'N/A')} - {args.get('remetente_tel', 'N/A')}
📱 **Destinatário:** {args.get('dest_nome', 'N/A')} - {args.get('dest_tel', 'N/A')}

📦 **Item:** {args.get('item_descricao', 'N/A')}
📏 **Distância:** {args.get('distance_km', 0):.1f} km
⏱️ **Tempo estimado:** {args.get('eta_min', 0)} min
🚦 **Trânsito:** {args.get('traffic_level', 'Normal')}

💰 **Valor total: R$ {final_amount:.2f}**

Confirma o pedido? Após a confirmação, enviaremos o PIX para pagamento.
"""
            
            return {
                "summary": summary_text.strip(),
                "amount_base": base_amount,
                "amount_final": final_amount,
                "markup_applied": markup_rate
            }
            
        except Exception as e:
            logger.error(f"Error summarizing order: {e}")
            return {"error": str(e)}
    
    async def _generate_pix_payment(self, args: Dict[str, Any]) -> Dict[str, Any]:
        """Generate PIX payment"""
        try:
            from ..pagseguro import PagSeguroClient
            from ...core.config import settings
            
            pagseguro = PagSeguroClient(
                token=settings.PAGSEGURO_TOKEN,
                email=settings.PAGSEGURO_EMAIL,
                sandbox=settings.PAGSEGURO_SANDBOX
            )
            
            amount = args.get("amount", 0)
            customer_name = args.get("customer_name", "Cliente")
            customer_phone = args.get("customer_phone", "")
            
            pix_data = await pagseguro.create_pix_payment(
                amount=amount,
                customer_name=customer_name,
                customer_phone=customer_phone,
                metadata=args.get("metadata", {})
            )
            
            return {
                "pix_code": pix_data.get("pix_code"),
                "qr_code": pix_data.get("qr_code"),
                "payment_id": pix_data.get("payment_id"),
                "expires_at": pix_data.get("expires_at")
            }
            
        except Exception as e:
            logger.error(f"Error generating PIX payment: {e}")
            return {"error": str(e)}
    
    def _get_time_of_day(self) -> str:
        """Get current time of day category"""
        hour = datetime.now().hour
        if 6 <= hour < 12:
            return "matutino"
        elif 12 <= hour < 18:
            return "vespertino"
        elif 18 <= hour < 22:
            return "noturno"
        else:
            return "madrugada"


class OTTOAssistant:
    """O.T.T.O Assistant wrapper with simplified interface"""
    
    def __init__(self, openai_client: OpenAIClient):
        self.client = openai_client
    
    async def start_conversation(self, user_id: str) -> str:
        """Start a new conversation with O.T.T.O"""
        try:
            thread_id = await self.client.create_thread()
            
            # Send welcome message
            welcome_msg = "Olá! Sou o O.T.T.O, seu assistente para entregas. Como posso ajudar você hoje?"
            
            return thread_id
            
        except Exception as e:
            logger.error(f"Error starting conversation: {e}")
            raise
    
    async def send_message(
        self,
        thread_id: str,
        message: str,
        user_id: Optional[str] = None,
        order_context: Optional[Dict[str, Any]] = None
    ) -> str:
        """Send message to O.T.T.O and get response"""
        try:
            metadata = {}
            if user_id:
                metadata["user_id"] = user_id
            if order_context:
                metadata["order_context"] = json.dumps(order_context)
            
            response = await self.client.send_message(
                thread_id=thread_id,
                message=message,
                user_id=user_id,
                metadata=metadata
            )
            
            return response
            
        except Exception as e:
            logger.error(f"Error sending message to O.T.T.O: {e}")
            return "Desculpe, estou com dificuldades técnicas. Tente novamente em alguns minutos."