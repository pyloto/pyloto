"""
Delivery model for tracking delivery execution
"""
from sqlalchemy import Column, Integer, String, Boolean, DateTime, Text, Enum as SQLEnum, ForeignKey, Numeric
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from enum import Enum
import uuid

from ..core.database import Base


class DeliveryStatus(str, Enum):
    """Delivery execution status"""
    ASSIGNED = "assigned"           # Driver assigned to delivery
    HEADING_TO_PICKUP = "heading_to_pickup"  # Driver going to pickup location
    AT_PICKUP = "at_pickup"        # Driver arrived at pickup
    PICKED_UP = "picked_up"        # Item collected
    IN_TRANSIT = "in_transit"      # On the way to delivery
    AT_DELIVERY = "at_delivery"    # Driver arrived at delivery location
    DELIVERED = "delivered"        # Successfully delivered
    FAILED = "failed"              # Delivery failed
    CANCELLED = "cancelled"        # Delivery cancelled


class Delivery(Base):
    """Delivery execution tracking"""
    __tablename__ = "deliveries"
    
    # Primary fields
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    
    # Relationships
    order_id = Column(String, ForeignKey("orders.id"), nullable=False, unique=True, index=True)
    driver_id = Column(String, ForeignKey("users.id"), nullable=False, index=True)
    
    # Status tracking
    status = Column(SQLEnum(DeliveryStatus), nullable=False, default=DeliveryStatus.ASSIGNED)
    
    # Driver location tracking
    current_latitude = Column(String(20), nullable=True)
    current_longitude = Column(String(20), nullable=True)
    last_location_update = Column(DateTime(timezone=True), nullable=True)
    
    # Estimated times
    estimated_pickup_time = Column(DateTime(timezone=True), nullable=True)
    estimated_delivery_time = Column(DateTime(timezone=True), nullable=True)
    
    # Actual timestamps
    assigned_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    heading_to_pickup_at = Column(DateTime(timezone=True), nullable=True)
    arrived_at_pickup_at = Column(DateTime(timezone=True), nullable=True)
    picked_up_at = Column(DateTime(timezone=True), nullable=True)
    in_transit_at = Column(DateTime(timezone=True), nullable=True)
    arrived_at_delivery_at = Column(DateTime(timezone=True), nullable=True)
    delivered_at = Column(DateTime(timezone=True), nullable=True)
    failed_at = Column(DateTime(timezone=True), nullable=True)
    cancelled_at = Column(DateTime(timezone=True), nullable=True)
    
    # Delivery proof
    delivery_photo_url = Column(String(500), nullable=True)
    delivery_signature_url = Column(String(500), nullable=True)
    delivery_notes = Column(Text, nullable=True)
    recipient_name = Column(String(200), nullable=True)
    
    # Failure information
    failure_reason = Column(String(500), nullable=True)
    failure_notes = Column(Text, nullable=True)
    retry_count = Column(Integer, default=0, nullable=False)
    
    # Rating and feedback
    driver_rating = Column(Integer, nullable=True)  # 1-5 rating by customer
    customer_rating = Column(Integer, nullable=True)  # 1-5 rating of customer by driver
    driver_feedback = Column(Text, nullable=True)
    customer_feedback = Column(Text, nullable=True)
    
    # Route optimization
    route_data = Column(Text, nullable=True)  # JSON with route information
    actual_distance_km = Column(Numeric(8, 2), nullable=True)
    actual_duration_minutes = Column(Integer, nullable=True)
    
    # Driver earnings
    driver_earnings = Column(Numeric(10, 2), nullable=True)
    driver_tip = Column(Numeric(10, 2), nullable=True)
    
    # System metadata
    metadata = Column(Text, nullable=True)  # JSON for additional data
    
    # Timestamps
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), onupdate=func.now(), nullable=True)
    
    # Relationships
    order = relationship("Order", back_populates="delivery")
    driver = relationship("User", back_populates="deliveries")
    
    def __repr__(self):
        return f"<Delivery(id={self.id}, order_id={self.order_id}, status={self.status})>"
    
    @property
    def is_active(self) -> bool:
        """Check if delivery is in progress"""
        active_states = [
            DeliveryStatus.ASSIGNED,
            DeliveryStatus.HEADING_TO_PICKUP,
            DeliveryStatus.AT_PICKUP,
            DeliveryStatus.PICKED_UP,
            DeliveryStatus.IN_TRANSIT,
            DeliveryStatus.AT_DELIVERY
        ]
        return self.status in active_states
    
    @property
    def is_completed(self) -> bool:
        """Check if delivery is completed"""
        return self.status in [DeliveryStatus.DELIVERED, DeliveryStatus.FAILED, DeliveryStatus.CANCELLED]
    
    def to_dict(self) -> dict:
        """Convert delivery to dictionary"""
        return {
            "id": self.id,
            "order_id": self.order_id,
            "driver_id": self.driver_id,
            "status": self.status.value,
            "current_latitude": self.current_latitude,
            "current_longitude": self.current_longitude,
            "last_location_update": self.last_location_update.isoformat() if self.last_location_update else None,
            "estimated_pickup_time": self.estimated_pickup_time.isoformat() if self.estimated_pickup_time else None,
            "estimated_delivery_time": self.estimated_delivery_time.isoformat() if self.estimated_delivery_time else None,
            "delivered_at": self.delivered_at.isoformat() if self.delivered_at else None,
            "driver_rating": self.driver_rating,
            "customer_rating": self.customer_rating,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }