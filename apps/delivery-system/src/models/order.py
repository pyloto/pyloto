"""
Order model for managing delivery requests
"""
from sqlalchemy import Column, Integer, String, Boolean, DateTime, Text, Enum as SQLEnum, ForeignKey, Numeric
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from enum import Enum
import uuid

from ..core.database import Base


class OrderStatus(str, Enum):
    """Order status states - follows FSM pattern"""
    DRAFT = "draft"                    # Initial state - collecting information
    PENDING_QUOTE = "pending_quote"    # Calculating price
    QUOTED = "quoted"                  # Price calculated, waiting for payment
    PENDING_PAYMENT = "pending_payment" # Payment being processed
    PAID = "paid"                      # Payment confirmed
    ASSIGNED = "assigned"              # Driver assigned
    PICKUP_PENDING = "pickup_pending"  # Driver on the way to pickup
    PICKED_UP = "picked_up"           # Item collected
    IN_TRANSIT = "in_transit"         # On the way to destination
    DELIVERED = "delivered"           # Successfully delivered
    CANCELLED = "cancelled"           # Cancelled by user/system
    FAILED = "failed"                 # Delivery failed
    REFUNDED = "refunded"             # Payment refunded


class OrderPriority(str, Enum):
    """Order priority levels"""
    LOW = "low"
    NORMAL = "normal"
    HIGH = "high"
    URGENT = "urgent"


class ItemCategory(str, Enum):
    """Categories for items being delivered"""
    FOOD = "food"
    MEDICINE = "medicine"
    DOCUMENTS = "documents"
    ELECTRONICS = "electronics"
    CLOTHING = "clothing"
    FLOWERS = "flowers"
    GROCERIES = "groceries"
    OTHER = "other"


class Order(Base):
    """Order model representing a delivery request"""
    __tablename__ = "orders"
    
    # Primary fields
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    order_number = Column(String(20), unique=True, index=True, nullable=False)  # Human-readable ID
    
    # Relationships
    consumer_id = Column(String, ForeignKey("users.id"), nullable=False, index=True)
    merchant_id = Column(String, ForeignKey("users.id"), nullable=True, index=True)
    assigned_driver_id = Column(String, ForeignKey("users.id"), nullable=True, index=True)
    
    # Status and priority
    status = Column(SQLEnum(OrderStatus), nullable=False, default=OrderStatus.DRAFT)
    priority = Column(SQLEnum(OrderPriority), nullable=False, default=OrderPriority.NORMAL)
    
    # Item information
    item_description = Column(Text, nullable=False)
    item_category = Column(SQLEnum(ItemCategory), nullable=False, default=ItemCategory.OTHER)
    item_weight_kg = Column(Numeric(5, 2), nullable=True)
    item_value = Column(Numeric(10, 2), nullable=True)  # Declared value for insurance
    item_photo_url = Column(String(500), nullable=True)
    special_instructions = Column(Text, nullable=True)
    
    # Pickup information
    pickup_contact_name = Column(String(200), nullable=False)
    pickup_contact_phone = Column(String(20), nullable=False)
    pickup_address_line1 = Column(String(255), nullable=False)
    pickup_address_line2 = Column(String(255), nullable=True)
    pickup_city = Column(String(100), nullable=False)
    pickup_state = Column(String(100), nullable=False)
    pickup_postal_code = Column(String(20), nullable=True)
    pickup_latitude = Column(String(20), nullable=True)
    pickup_longitude = Column(String(20), nullable=True)
    pickup_instructions = Column(Text, nullable=True)
    
    # Delivery information
    delivery_contact_name = Column(String(200), nullable=False)
    delivery_contact_phone = Column(String(20), nullable=False)
    delivery_address_line1 = Column(String(255), nullable=False)
    delivery_address_line2 = Column(String(255), nullable=True)
    delivery_city = Column(String(100), nullable=False)
    delivery_state = Column(String(100), nullable=False)
    delivery_postal_code = Column(String(20), nullable=True)
    delivery_latitude = Column(String(20), nullable=True)
    delivery_longitude = Column(String(20), nullable=True)
    delivery_instructions = Column(Text, nullable=True)
    
    # Route and pricing information
    distance_km = Column(Numeric(8, 2), nullable=True)
    estimated_duration_minutes = Column(Integer, nullable=True)
    base_price = Column(Numeric(10, 2), nullable=True)
    final_price = Column(Numeric(10, 2), nullable=True)
    currency = Column(String(3), default="BRL", nullable=False)
    
    # Pricing factors (for transparency and debugging)
    price_factors = Column(Text, nullable=True)  # JSON with pricing breakdown
    
    # Scheduling
    pickup_scheduled_at = Column(DateTime(timezone=True), nullable=True)
    delivery_scheduled_at = Column(DateTime(timezone=True), nullable=True)
    is_scheduled = Column(Boolean, default=False, nullable=False)
    
    # Tracking timestamps
    quote_generated_at = Column(DateTime(timezone=True), nullable=True)
    payment_confirmed_at = Column(DateTime(timezone=True), nullable=True)
    driver_assigned_at = Column(DateTime(timezone=True), nullable=True)
    pickup_started_at = Column(DateTime(timezone=True), nullable=True)
    picked_up_at = Column(DateTime(timezone=True), nullable=True)
    delivery_started_at = Column(DateTime(timezone=True), nullable=True)
    delivered_at = Column(DateTime(timezone=True), nullable=True)
    cancelled_at = Column(DateTime(timezone=True), nullable=True)
    
    # External integrations
    whatsapp_conversation_id = Column(String(100), nullable=True)
    openai_thread_id = Column(String(100), nullable=True)
    google_places_pickup_id = Column(String(200), nullable=True)
    google_places_delivery_id = Column(String(200), nullable=True)
    
    # Additional metadata
    source = Column(String(50), default="whatsapp", nullable=False)  # whatsapp, web, api
    user_agent = Column(String(500), nullable=True)
    ip_address = Column(String(45), nullable=True)
    
    # Rating and feedback
    consumer_rating = Column(Integer, nullable=True)  # 1-5
    driver_rating = Column(Integer, nullable=True)    # 1-5
    consumer_feedback = Column(Text, nullable=True)
    driver_feedback = Column(Text, nullable=True)
    
    # System metadata
    metadata = Column(Text, nullable=True)  # JSON for flexible additional data
    internal_notes = Column(Text, nullable=True)  # Admin notes
    
    # Timestamps
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), onupdate=func.now(), nullable=True)
    deleted_at = Column(DateTime(timezone=True), nullable=True)  # Soft delete
    
    # Relationships
    consumer = relationship("User", foreign_keys=[consumer_id], back_populates="orders_as_consumer")
    merchant = relationship("User", foreign_keys=[merchant_id], back_populates="orders_as_merchant")
    delivery = relationship("Delivery", back_populates="order", uselist=False)
    payment = relationship("Payment", back_populates="order", uselist=False)
    notifications = relationship("Notification", back_populates="order")
    
    def __repr__(self):
        return f"<Order(id={self.id}, number={self.order_number}, status={self.status})>"
    
    @property
    def full_pickup_address(self) -> str:
        """Get formatted pickup address"""
        parts = [self.pickup_address_line1]
        if self.pickup_address_line2:
            parts.append(self.pickup_address_line2)
        parts.extend([self.pickup_city, self.pickup_state])
        if self.pickup_postal_code:
            parts.append(self.pickup_postal_code)
        return ", ".join(parts)
    
    @property
    def full_delivery_address(self) -> str:
        """Get formatted delivery address"""
        parts = [self.delivery_address_line1]
        if self.delivery_address_line2:
            parts.append(self.delivery_address_line2)
        parts.extend([self.delivery_city, self.delivery_state])
        if self.delivery_postal_code:
            parts.append(self.delivery_postal_code)
        return ", ".join(parts)
    
    @property
    def is_active(self) -> bool:
        """Check if order is in an active state"""
        active_states = [
            OrderStatus.QUOTED,
            OrderStatus.PENDING_PAYMENT,
            OrderStatus.PAID,
            OrderStatus.ASSIGNED,
            OrderStatus.PICKUP_PENDING,
            OrderStatus.PICKED_UP,
            OrderStatus.IN_TRANSIT
        ]
        return self.status in active_states
    
    @property
    def is_completed(self) -> bool:
        """Check if order is completed"""
        completed_states = [
            OrderStatus.DELIVERED,
            OrderStatus.CANCELLED,
            OrderStatus.FAILED,
            OrderStatus.REFUNDED
        ]
        return self.status in completed_states
    
    def to_dict(self, include_sensitive: bool = False) -> dict:
        """Convert order to dictionary"""
        data = {
            "id": self.id,
            "order_number": self.order_number,
            "status": self.status.value,
            "priority": self.priority.value,
            "item_description": self.item_description,
            "item_category": self.item_category.value,
            "pickup_address": self.full_pickup_address,
            "delivery_address": self.full_delivery_address,
            "distance_km": float(self.distance_km) if self.distance_km else None,
            "estimated_duration_minutes": self.estimated_duration_minutes,
            "final_price": float(self.final_price) if self.final_price else None,
            "currency": self.currency,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }
        
        if include_sensitive:
            data.update({
                "pickup_contact_name": self.pickup_contact_name,
                "pickup_contact_phone": self.pickup_contact_phone,
                "delivery_contact_name": self.delivery_contact_name,
                "delivery_contact_phone": self.delivery_contact_phone,
                "consumer_id": self.consumer_id,
                "merchant_id": self.merchant_id,
                "assigned_driver_id": self.assigned_driver_id,
            })
        
        return data