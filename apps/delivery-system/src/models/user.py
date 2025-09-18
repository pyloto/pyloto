"""
User model for authentication and user management
"""
from sqlalchemy import Column, Integer, String, Boolean, DateTime, Text, Enum as SQLEnum
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from enum import Enum
import uuid

from ..core.database import Base


class UserRole(str, Enum):
    """User roles in the system"""
    CONSUMER = "consumer"      # End users who request deliveries
    MERCHANT = "merchant"      # Store owners who need deliveries
    DRIVER = "driver"         # Delivery drivers
    ADMIN = "admin"           # System administrators
    SUPPORT = "support"       # Customer support


class UserStatus(str, Enum):
    """User account status"""
    ACTIVE = "active"
    INACTIVE = "inactive"
    SUSPENDED = "suspended"
    PENDING_VERIFICATION = "pending_verification"


class User(Base):
    """User model with comprehensive fields for all user types"""
    __tablename__ = "users"
    
    # Primary fields
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    email = Column(String(255), unique=True, index=True, nullable=False)
    phone = Column(String(20), index=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    
    # Profile information
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    full_name = Column(String(200), nullable=True)  # Computed field
    profile_image = Column(String(500), nullable=True)
    
    # Role and status
    role = Column(SQLEnum(UserRole), nullable=False, default=UserRole.CONSUMER)
    status = Column(SQLEnum(UserStatus), nullable=False, default=UserStatus.PENDING_VERIFICATION)
    
    # Verification
    email_verified = Column(Boolean, default=False, nullable=False)
    phone_verified = Column(Boolean, default=False, nullable=False)
    verification_token = Column(String(255), nullable=True)
    
    # Security
    is_active = Column(Boolean, default=True, nullable=False)
    is_superuser = Column(Boolean, default=False, nullable=False)
    failed_login_attempts = Column(Integer, default=0, nullable=False)
    last_login = Column(DateTime(timezone=True), nullable=True)
    password_reset_token = Column(String(255), nullable=True)
    password_reset_expires = Column(DateTime(timezone=True), nullable=True)
    
    # Address information (primary address)
    address_line1 = Column(String(255), nullable=True)
    address_line2 = Column(String(255), nullable=True)
    city = Column(String(100), nullable=True)
    state = Column(String(100), nullable=True)
    postal_code = Column(String(20), nullable=True)
    country = Column(String(100), default="Brasil", nullable=False)
    
    # Geolocation
    latitude = Column(String(20), nullable=True)
    longitude = Column(String(20), nullable=True)
    
    # Driver-specific fields
    driver_license = Column(String(50), nullable=True)
    vehicle_type = Column(String(50), nullable=True)  # motorcycle, car, bicycle
    vehicle_model = Column(String(100), nullable=True)
    vehicle_plate = Column(String(20), nullable=True)
    driver_rating = Column(String(5), default="5.0", nullable=True)
    driver_status = Column(String(20), default="offline", nullable=True)  # online, offline, busy
    
    # Merchant-specific fields
    business_name = Column(String(200), nullable=True)
    business_type = Column(String(100), nullable=True)
    tax_id = Column(String(50), nullable=True)  # CNPJ or CPF
    business_description = Column(Text, nullable=True)
    
    # Preferences and settings
    language = Column(String(10), default="pt-BR", nullable=False)
    timezone = Column(String(50), default="America/Sao_Paulo", nullable=False)
    notification_preferences = Column(Text, nullable=True)  # JSON string
    
    # WhatsApp integration
    whatsapp_id = Column(String(50), nullable=True)
    whatsapp_verified = Column(Boolean, default=False, nullable=False)
    
    # Metadata
    metadata = Column(Text, nullable=True)  # JSON for flexible additional data
    notes = Column(Text, nullable=True)  # Admin notes
    
    # Timestamps
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), onupdate=func.now(), nullable=True)
    deleted_at = Column(DateTime(timezone=True), nullable=True)  # Soft delete
    
    # Relationships
    orders_as_consumer = relationship("Order", foreign_keys="Order.consumer_id", back_populates="consumer")
    orders_as_merchant = relationship("Order", foreign_keys="Order.merchant_id", back_populates="merchant")
    deliveries = relationship("Delivery", back_populates="driver")
    notifications = relationship("Notification", back_populates="user")
    
    def __repr__(self):
        return f"<User(id={self.id}, email={self.email}, role={self.role})>"
    
    @property
    def display_name(self) -> str:
        """Get display name for the user"""
        if self.business_name and self.role == UserRole.MERCHANT:
            return self.business_name
        return f"{self.first_name} {self.last_name}".strip()
    
    @property
    def is_driver_available(self) -> bool:
        """Check if driver is available for deliveries"""
        return (
            self.role == UserRole.DRIVER and
            self.status == UserStatus.ACTIVE and
            self.driver_status == "online"
        )
    
    def to_dict(self, include_sensitive: bool = False) -> dict:
        """Convert user to dictionary"""
        data = {
            "id": self.id,
            "email": self.email,
            "phone": self.phone,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "display_name": self.display_name,
            "role": self.role.value,
            "status": self.status.value,
            "email_verified": self.email_verified,
            "phone_verified": self.phone_verified,
            "is_active": self.is_active,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }
        
        # Add role-specific fields
        if self.role == UserRole.DRIVER:
            data.update({
                "vehicle_type": self.vehicle_type,
                "vehicle_model": self.vehicle_model,
                "driver_rating": self.driver_rating,
                "driver_status": self.driver_status,
            })
        
        if self.role == UserRole.MERCHANT:
            data.update({
                "business_name": self.business_name,
                "business_type": self.business_type,
            })
        
        if include_sensitive:
            data.update({
                "address_line1": self.address_line1,
                "city": self.city,
                "state": self.state,
                "latitude": self.latitude,
                "longitude": self.longitude,
            })
        
        return data