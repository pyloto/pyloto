"""
WhatsApp webhook endpoint for O.T.T.O integration
"""
from fastapi import APIRouter, Request, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
import logging
from typing import Dict, Any

from ...core import get_async_session
from ...services.otto import OTTOService
from ...services.auth import AuthService

logger = logging.getLogger(__name__)
router = APIRouter()


@router.get("/whatsapp")
async def whatsapp_webhook_verification(request: Request):
    """WhatsApp webhook verification"""
    try:
        # Get verification parameters
        hub_mode = request.query_params.get("hub.mode")
        hub_challenge = request.query_params.get("hub.challenge")
        hub_verify_token = request.query_params.get("hub.verify_token")
        
        # Verify token (you should set this in your environment)
        expected_token = "pyloto_webhook_token_2025"  # TODO: Move to settings
        
        if hub_mode == "subscribe" and hub_verify_token == expected_token:
            logger.info("WhatsApp webhook verified successfully")
            return int(hub_challenge)
        else:
            logger.warning(f"WhatsApp webhook verification failed: mode={hub_mode}, token={hub_verify_token}")
            raise HTTPException(status_code=403, detail="Verification failed")
            
    except Exception as e:
        logger.error(f"WhatsApp webhook verification error: {e}")
        raise HTTPException(status_code=500, detail="Verification error")


@router.post("/whatsapp")
async def whatsapp_webhook_handler(
    request: Request,
    db: AsyncSession = Depends(get_async_session)
):
    """Handle incoming WhatsApp messages"""
    try:
        # Get webhook data
        webhook_data = await request.json()
        logger.info(f"Received WhatsApp webhook: {webhook_data}")
        
        # Initialize services
        otto_service = OTTOService()
        auth_service = AuthService(db)
        
        # Parse webhook data
        from ....packages.integrations.whatsapp import WhatsAppClient
        whatsapp_client = WhatsAppClient("", "", "")  # Dummy client just for parsing
        parsed_data = whatsapp_client.parse_webhook(webhook_data)
        
        if not parsed_data:
            logger.warning("No parseable data in WhatsApp webhook")
            return {"status": "ignored"}
        
        if parsed_data["type"] == "message":
            await _handle_incoming_message(parsed_data, otto_service, auth_service)
        elif parsed_data["type"] == "status":
            await _handle_status_update(parsed_data)
        
        return {"status": "processed"}
        
    except Exception as e:
        logger.error(f"WhatsApp webhook handler error: {e}")
        # Don't raise exception to avoid webhook retries
        return {"status": "error", "message": str(e)}


async def _handle_incoming_message(
    message_data: Dict[str, Any],
    otto_service: OTTOService,
    auth_service: AuthService
):
    """Handle incoming WhatsApp message"""
    try:
        phone_number = message_data["from"]
        message_id = message_data["message_id"]
        message_type = message_data["message_type"]
        
        # Get or create user
        user = await auth_service.get_user_by_phone(phone_number)
        if not user:
            # Create new user with phone number
            user = await auth_service.create_user_from_phone(phone_number)
        
        # Handle different message types
        if message_type == "text":
            message_text = message_data["text"]
            await otto_service.process_whatsapp_message(
                phone_number=phone_number,
                message_text=message_text,
                message_id=message_id,
                user=user
            )
        
        elif message_type == "interactive":
            # Handle button clicks
            interactive_data = message_data["interactive"]
            if interactive_data.get("type") == "button_reply":
                button_id = interactive_data["button_reply"]["id"]
                await otto_service.handle_button_interaction(
                    phone_number=phone_number,
                    button_id=button_id,
                    user=user
                )
        
        elif message_type == "location":
            # Handle location sharing
            location_data = message_data["location"]
            location_text = f"Localização recebida: {location_data['latitude']}, {location_data['longitude']}"
            await otto_service.process_whatsapp_message(
                phone_number=phone_number,
                message_text=location_text,
                message_id=message_id,
                user=user
            )
        
        elif message_type == "image":
            # Handle image uploads (item photos)
            image_text = "Imagem recebida. Descreva o item que precisa ser entregue."
            await otto_service.process_whatsapp_message(
                phone_number=phone_number,
                message_text=image_text,
                message_id=message_id,
                user=user
            )
        
        else:
            logger.warning(f"Unhandled message type: {message_type}")
            
    except Exception as e:
        logger.error(f"Error handling incoming message: {e}")


async def _handle_status_update(status_data: Dict[str, Any]):
    """Handle WhatsApp message status updates"""
    try:
        message_id = status_data["message_id"]
        status = status_data["status"]
        
        logger.info(f"Message {message_id} status: {status}")
        
        # You can update notification status in database here
        # For now, just log it
        
    except Exception as e:
        logger.error(f"Error handling status update: {e}")


@router.post("/whatsapp/send")
async def send_whatsapp_message(
    request: Request,
    db: AsyncSession = Depends(get_async_session)
):
    """Send WhatsApp message (for testing or admin use)"""
    try:
        data = await request.json()
        phone_number = data.get("phone_number")
        message = data.get("message")
        
        if not phone_number or not message:
            raise HTTPException(
                status_code=400,
                detail="phone_number and message are required"
            )
        
        otto_service = OTTOService()
        
        if otto_service.whatsapp_client:
            result = await otto_service.whatsapp_client.send_text_message(
                to=phone_number,
                message=message
            )
            return {"status": "sent", "result": result}
        else:
            raise HTTPException(
                status_code=503,
                detail="WhatsApp client not configured"
            )
            
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error sending WhatsApp message: {e}")
        raise HTTPException(status_code=500, detail=str(e))