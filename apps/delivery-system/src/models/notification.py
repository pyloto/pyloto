"""
Notification model for managing all types of notifications
"""
from sqlalchemy import Column, Integer, String, Boolean, DateTime, Text, Enum as SQLEnum, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from enum import Enum
import uuid

from ..core.database import Base


class NotificationType(str, Enum):
    """Types of notifications"""
    SMS = "sms"
    EMAIL = "email"
    WHATSAPP = "whatsapp"
    PUSH = "push"
    IN_APP = "in_app"
    WEBHOOK = "webhook"


class NotificationStatus(str, Enum):
    """Notification delivery status"""
    PENDING = "pending"         # Queued for sending
    SENDING = "sending"         # Being sent
    SENT = "sent"              # Successfully sent
    DELIVERED = "delivered"     # Confirmed delivered (if supported)
    READ = "read"              # Confirmed read (if supported)
    FAILED = "failed"          # Failed to send
    CANCELLED = "cancelled"    # Cancelled before sending


class Notification(Base):
    """Notification tracking and management"""
    __tablename__ = "notifications"
    
    # Primary fields
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    
    # Relationships
    user_id = Column(String, ForeignKey("users.id"), nullable=False, index=True)
    order_id = Column(String, ForeignKey("orders.id"), nullable=True, index=True)
    
    # Notification details
    type = Column(SQLEnum(NotificationType), nullable=False)
    status = Column(SQLEnum(NotificationStatus), nullable=False, default=NotificationStatus.PENDING)
    
    # Content
    title = Column(String(200), nullable=True)
    message = Column(Text, nullable=False)
    
    # Recipient information
    recipient_phone = Column(String(20), nullable=True)
    recipient_email = Column(String(255), nullable=True)
    recipient_whatsapp = Column(String(50), nullable=True)
    
    # Delivery tracking
    external_id = Column(String(200), nullable=True)  # ID from external service
    external_status = Column(String(50), nullable=True)
    external_response = Column(Text, nullable=True)  # JSON response
    
    # Scheduling
    scheduled_at = Column(DateTime(timezone=True), nullable=True)
    sent_at = Column(DateTime(timezone=True), nullable=True)
    delivered_at = Column(DateTime(timezone=True), nullable=True)
    read_at = Column(DateTime(timezone=True), nullable=True)
    failed_at = Column(DateTime(timezone=True), nullable=True)
    
    # Retry logic
    retry_count = Column(Integer, default=0, nullable=False)
    max_retries = Column(Integer, default=3, nullable=False)
    next_retry_at = Column(DateTime(timezone=True), nullable=True)
    
    # Error tracking
    error_message = Column(String(500), nullable=True)
    error_code = Column(String(50), nullable=True)
    
    # Template and personalization
    template_id = Column(String(100), nullable=True)
    template_variables = Column(Text, nullable=True)  # JSON with variables
    
    # Priority and categorization
    priority = Column(Integer, default=5, nullable=False)  # 1-10, 10 being highest
    category = Column(String(50), nullable=True)  # order_update, marketing, etc.
    
    # User interaction tracking
    clicked = Column(Boolean, default=False, nullable=False)
    clicked_at = Column(DateTime(timezone=True), nullable=True)
    click_url = Column(String(500), nullable=True)
    
    # System metadata
    metadata = Column(Text, nullable=True)  # JSON for additional data
    
    # Timestamps
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), onupdate=func.now(), nullable=True)
    
    # Relationships
    user = relationship("User", back_populates="notifications")
    order = relationship("Order", back_populates="notifications")
    
    def __repr__(self):
        return f"<Notification(id={self.id}, type={self.type}, status={self.status})>"
    
    @property
    def is_pending(self) -> bool:
        """Check if notification is pending"""
        return self.status in [NotificationStatus.PENDING, NotificationStatus.SENDING]
    
    @property
    def is_sent(self) -> bool:
        """Check if notification was sent"""
        return self.status in [
            NotificationStatus.SENT,
            NotificationStatus.DELIVERED,
            NotificationStatus.READ
        ]
    
    @property
    def is_failed(self) -> bool:
        """Check if notification failed"""
        return self.status in [NotificationStatus.FAILED, NotificationStatus.CANCELLED]
    
    @property
    def can_retry(self) -> bool:
        """Check if notification can be retried"""
        return (
            self.status == NotificationStatus.FAILED and
            self.retry_count < self.max_retries
        )
    
    def to_dict(self) -> dict:
        """Convert notification to dictionary"""
        return {
            "id": self.id,
            "user_id": self.user_id,
            "order_id": self.order_id,
            "type": self.type.value,
            "status": self.status.value,
            "title": self.title,
            "message": self.message,
            "scheduled_at": self.scheduled_at.isoformat() if self.scheduled_at else None,
            "sent_at": self.sent_at.isoformat() if self.sent_at else None,
            "delivered_at": self.delivered_at.isoformat() if self.delivered_at else None,
            "read_at": self.read_at.isoformat() if self.read_at else None,
            "failed_at": self.failed_at.isoformat() if self.failed_at else None,
            "retry_count": self.retry_count,
            "priority": self.priority,
            "category": self.category,
            "clicked": self.clicked,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }