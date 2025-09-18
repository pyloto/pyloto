"""
Main API router for v1 endpoints
"""
from fastapi import APIRouter

from .endpoints import auth, orders, users, deliveries, payments, notifications, admin, webhooks

# Create main API router
api_router = APIRouter()

# Include all endpoint routers
api_router.include_router(auth.router, prefix="/auth", tags=["Authentication"])
api_router.include_router(users.router, prefix="/users", tags=["Users"])
api_router.include_router(orders.router, prefix="/orders", tags=["Orders"])
api_router.include_router(deliveries.router, prefix="/deliveries", tags=["Deliveries"])
api_router.include_router(payments.router, prefix="/payments", tags=["Payments"])  
api_router.include_router(notifications.router, prefix="/notifications", tags=["Notifications"])
api_router.include_router(admin.router, prefix="/admin", tags=["Admin"])
api_router.include_router(webhooks.router, prefix="/webhooks", tags=["Webhooks"])


@api_router.get("/")
async def api_root():
    """API root endpoint"""
    return {
        "message": "Pyloto Delivery System API v1",
        "version": "1.0.0",
        "endpoints": {
            "auth": "/auth",
            "users": "/users", 
            "orders": "/orders",
            "deliveries": "/deliveries",
            "payments": "/payments",
            "notifications": "/notifications",
            "admin": "/admin",
            "webhooks": "/webhooks"
        }
    }