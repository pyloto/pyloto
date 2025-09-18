"""
WhatsApp Business API Integration
Handles all WhatsApp messaging functionality
"""
import httpx
import json
from typing import Optional, Dict, Any, List
import logging
from datetime import datetime

logger = logging.getLogger(__name__)


class WhatsAppClient:
    """WhatsApp Business API client"""
    
    def __init__(self, api_url: str, token: str, phone_number_id: str):
        self.api_url = api_url.rstrip('/')
        self.token = token
        self.phone_number_id = phone_number_id
        self.headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }
    
    async def send_text_message(
        self,
        to: str,
        message: str,
        context_message_id: Optional[str] = None
    ) -> Dict[str, Any]:
        """Send a text message"""
        try:
            payload = {
                "messaging_product": "whatsapp",
                "recipient_type": "individual",
                "to": to,
                "type": "text",
                "text": {
                    "body": message
                }
            }
            
            if context_message_id:
                payload["context"] = {
                    "message_id": context_message_id
                }
            
            async with httpx.AsyncClient() as client:
                response = await client.post(
                    f"{self.api_url}/{self.phone_number_id}/messages",
                    headers=self.headers,
                    json=payload
                )
                
                if response.status_code == 200:
                    return response.json()
                else:
                    logger.error(f"WhatsApp API error: {response.status_code} - {response.text}")
                    return {"error": response.text}
                    
        except Exception as e:
            logger.error(f"Error sending WhatsApp message: {e}")
            return {"error": str(e)}
    
    async def send_template_message(
        self,
        to: str,
        template_name: str,
        language_code: str = "pt_BR",
        parameters: Optional[List[str]] = None
    ) -> Dict[str, Any]:
        """Send a template message"""
        try:
            components = []
            
            if parameters:
                components.append({
                    "type": "body",
                    "parameters": [{"type": "text", "text": param} for param in parameters]
                })
            
            payload = {
                "messaging_product": "whatsapp",
                "recipient_type": "individual",
                "to": to,
                "type": "template",
                "template": {
                    "name": template_name,
                    "language": {
                        "code": language_code
                    },
                    "components": components
                }
            }
            
            async with httpx.AsyncClient() as client:
                response = await client.post(
                    f"{self.api_url}/{self.phone_number_id}/messages",
                    headers=self.headers,
                    json=payload
                )
                
                if response.status_code == 200:
                    return response.json()
                else:
                    logger.error(f"WhatsApp template API error: {response.status_code} - {response.text}")
                    return {"error": response.text}
                    
        except Exception as e:
            logger.error(f"Error sending WhatsApp template: {e}")
            return {"error": str(e)}
    
    async def send_interactive_message(
        self,
        to: str,
        body_text: str,
        buttons: List[Dict[str, str]],
        header_text: Optional[str] = None,
        footer_text: Optional[str] = None
    ) -> Dict[str, Any]:
        """Send an interactive message with buttons"""
        try:
            interactive_data = {
                "type": "button",
                "body": {
                    "text": body_text
                },
                "action": {
                    "buttons": [
                        {
                            "type": "reply",
                            "reply": {
                                "id": button["id"],
                                "title": button["title"]
                            }
                        }
                        for button in buttons[:3]  # WhatsApp allows max 3 buttons
                    ]
                }
            }
            
            if header_text:
                interactive_data["header"] = {
                    "type": "text",
                    "text": header_text
                }
            
            if footer_text:
                interactive_data["footer"] = {
                    "text": footer_text
                }
            
            payload = {
                "messaging_product": "whatsapp",
                "recipient_type": "individual",
                "to": to,
                "type": "interactive",
                "interactive": interactive_data
            }
            
            async with httpx.AsyncClient() as client:
                response = await client.post(
                    f"{self.api_url}/{self.phone_number_id}/messages",
                    headers=self.headers,
                    json=payload
                )
                
                if response.status_code == 200:
                    return response.json()
                else:
                    logger.error(f"WhatsApp interactive API error: {response.status_code} - {response.text}")
                    return {"error": response.text}
                    
        except Exception as e:
            logger.error(f"Error sending WhatsApp interactive message: {e}")
            return {"error": str(e)}
    
    async def send_location_message(
        self,
        to: str,
        latitude: float,
        longitude: float,
        name: Optional[str] = None,
        address: Optional[str] = None
    ) -> Dict[str, Any]:
        """Send a location message"""
        try:
            location_data = {
                "latitude": latitude,
                "longitude": longitude
            }
            
            if name:
                location_data["name"] = name
            if address:
                location_data["address"] = address
            
            payload = {
                "messaging_product": "whatsapp",
                "recipient_type": "individual",
                "to": to,
                "type": "location",
                "location": location_data
            }
            
            async with httpx.AsyncClient() as client:
                response = await client.post(
                    f"{self.api_url}/{self.phone_number_id}/messages",
                    headers=self.headers,
                    json=payload
                )
                
                if response.status_code == 200:
                    return response.json()
                else:
                    logger.error(f"WhatsApp location API error: {response.status_code} - {response.text}")
                    return {"error": response.text}
                    
        except Exception as e:
            logger.error(f"Error sending WhatsApp location: {e}")
            return {"error": str(e)}
    
    async def mark_as_read(self, message_id: str) -> Dict[str, Any]:
        """Mark a message as read"""
        try:
            payload = {
                "messaging_product": "whatsapp",
                "status": "read",
                "message_id": message_id
            }
            
            async with httpx.AsyncClient() as client:
                response = await client.post(
                    f"{self.api_url}/{self.phone_number_id}/messages",
                    headers=self.headers,
                    json=payload
                )
                
                if response.status_code == 200:
                    return response.json()
                else:
                    logger.error(f"WhatsApp read API error: {response.status_code} - {response.text}")
                    return {"error": response.text}
                    
        except Exception as e:
            logger.error(f"Error marking WhatsApp message as read: {e}")
            return {"error": str(e)}
    
    def parse_webhook(self, webhook_data: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """Parse incoming webhook data"""
        try:
            if "entry" not in webhook_data:
                return None
            
            for entry in webhook_data["entry"]:
                if "changes" not in entry:
                    continue
                    
                for change in entry["changes"]:
                    if change.get("field") != "messages":
                        continue
                    
                    value = change.get("value", {})
                    
                    # Handle incoming messages
                    if "messages" in value:
                        for message in value["messages"]:
                            return {
                                "type": "message",
                                "message_id": message.get("id"),
                                "from": message.get("from"),
                                "timestamp": message.get("timestamp"),
                                "message_type": message.get("type"),
                                "text": message.get("text", {}).get("body") if message.get("type") == "text" else None,
                                "interactive": message.get("interactive") if message.get("type") == "interactive" else None,
                                "location": message.get("location") if message.get("type") == "location" else None,
                                "image": message.get("image") if message.get("type") == "image" else None,
                                "document": message.get("document") if message.get("type") == "document" else None,
                            }
                    
                    # Handle status updates
                    if "statuses" in value:
                        for status in value["statuses"]:
                            return {
                                "type": "status",
                                "message_id": status.get("id"),
                                "recipient_id": status.get("recipient_id"),
                                "status": status.get("status"),
                                "timestamp": status.get("timestamp"),
                                "conversation": status.get("conversation"),
                                "pricing": status.get("pricing")
                            }
            
            return None
            
        except Exception as e:
            logger.error(f"Error parsing WhatsApp webhook: {e}")
            return None


class WhatsAppMessageTemplates:
    """Pre-defined message templates for common scenarios"""
    
    @staticmethod
    def welcome_message(user_name: str = "Cliente") -> str:
        return f"""Olá {user_name}! 👋

Sou o O.T.T.O, seu assistente virtual da Pyloto! Estou aqui para ajudar você com suas entregas de forma rápida e inteligente.

Como posso ajudar você hoje?

• 📦 Solicitar uma entrega
• 📍 Rastrear um pedido
• 💰 Ver preços
• ❓ Tirar dúvidas

Digite sua mensagem ou escolha uma das opções! 😊"""

    @staticmethod  
    def order_confirmation(order_number: str, pickup_address: str, delivery_address: str, price: float) -> str:
        return f"""✅ **Pedido Confirmado!**

📋 **Número:** {order_number}
📍 **Coleta:** {pickup_address}
🎯 **Entrega:** {delivery_address}
💰 **Valor:** R$ {price:.2f}

Estamos procurando um entregador para você! Você receberá atualizações em tempo real sobre o status da sua entrega.

Obrigado por escolher a Pyloto! 🚀"""

    @staticmethod
    def driver_assigned(driver_name: str, vehicle_info: str, eta_minutes: int) -> str:
        return f"""🚀 **Entregador a caminho!**

👤 **Entregador:** {driver_name}
🏍️ **Veículo:** {vehicle_info}
⏱️ **Chegada estimada:** {eta_minutes} minutos

O entregador está indo buscar seu pedido. Você pode acompanhar a localização em tempo real pelo nosso painel.

Em caso de dúvidas, responda esta mensagem! 📱"""

    @staticmethod
    def delivery_completed(order_number: str) -> str:
        return f"""🎉 **Entrega Realizada!**

📋 **Pedido:** {order_number}
✅ **Status:** Entregue com sucesso!

Esperamos que tudo tenha corrido bem! Sua avaliação é muito importante para nós.

Como foi sua experiência? 
⭐ Excelente
⭐ Boa  
⭐ Regular
⭐ Ruim

Obrigado por usar a Pyloto! 🚀"""

    @staticmethod
    def payment_pix_generated(pix_code: str, amount: float, expiration_minutes: int = 30) -> str:
        return f"""💰 **PIX Gerado!**

**Valor:** R$ {amount:.2f}
**Vencimento:** {expiration_minutes} minutos

**Código PIX (Copia e Cola):**
```
{pix_code}
```

📱 Abra seu app bancário, vá em PIX e cole o código acima.

⚠️ Após o pagamento, sua entrega será automaticamente iniciada!

Dúvidas? Responda esta mensagem! 😊"""