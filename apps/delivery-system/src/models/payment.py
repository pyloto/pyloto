"""
Payment model for handling order payments
"""
from sqlalchemy import Column, Integer, String, Boolean, DateTime, Text, Enum as SQLEnum, ForeignKey, Numeric
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from enum import Enum
import uuid

from ..core.database import Base


class PaymentStatus(str, Enum):
    """Payment processing status"""
    PENDING = "pending"           # Payment initiated
    PROCESSING = "processing"     # Being processed by gateway
    COMPLETED = "completed"       # Successfully processed
    FAILED = "failed"            # Payment failed
    CANCELLED = "cancelled"      # Cancelled by user
    REFUNDED = "refunded"        # Refunded to user
    PARTIALLY_REFUNDED = "partially_refunded"  # Partial refund


class PaymentMethod(str, Enum):
    """Payment methods supported"""
    PIX = "pix"                  # Brazilian instant payment
    CREDIT_CARD = "credit_card"  # Credit card
    DEBIT_CARD = "debit_card"    # Debit card
    BOLETO = "boleto"           # Brazilian banking ticket
    WALLET = "wallet"           # Digital wallet (balance)


class Payment(Base):
    """Payment processing and tracking"""
    __tablename__ = "payments"
    
    # Primary fields
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    
    # Relationships
    order_id = Column(String, ForeignKey("orders.id"), nullable=False, unique=True, index=True)
    
    # Payment details
    method = Column(SQLEnum(PaymentMethod), nullable=False, default=PaymentMethod.PIX)
    status = Column(SQLEnum(PaymentStatus), nullable=False, default=PaymentStatus.PENDING)
    
    # Amounts (in cents to avoid floating point issues)
    amount_cents = Column(Integer, nullable=False)
    currency = Column(String(3), default="BRL", nullable=False)
    
    # Gateway information
    gateway = Column(String(50), nullable=False, default="pagseguro")  # pagseguro, stripe, etc.
    gateway_transaction_id = Column(String(200), nullable=True, index=True)
    gateway_reference_id = Column(String(200), nullable=True)
    gateway_status = Column(String(50), nullable=True)
    gateway_response = Column(Text, nullable=True)  # JSON response from gateway
    
    # PIX specific fields
    pix_qr_code = Column(Text, nullable=True)  # PIX QR code string
    pix_code = Column(Text, nullable=True)     # PIX copy-paste code
    pix_expiration = Column(DateTime(timezone=True), nullable=True)
    
    # Card specific fields (if using cards)
    card_brand = Column(String(50), nullable=True)
    card_last_digits = Column(String(4), nullable=True)
    installments = Column(Integer, default=1, nullable=False)
    
    # Fees and costs
    gateway_fee_cents = Column(Integer, default=0, nullable=False)
    platform_fee_cents = Column(Integer, default=0, nullable=False)
    net_amount_cents = Column(Integer, nullable=True)  # Amount after fees
    
    # Processing timestamps
    initiated_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    processing_started_at = Column(DateTime(timezone=True), nullable=True)
    completed_at = Column(DateTime(timezone=True), nullable=True)
    failed_at = Column(DateTime(timezone=True), nullable=True)
    cancelled_at = Column(DateTime(timezone=True), nullable=True)
    
    # Refund information
    refund_amount_cents = Column(Integer, default=0, nullable=False)
    refund_reason = Column(String(500), nullable=True)
    refunded_at = Column(DateTime(timezone=True), nullable=True)
    refund_gateway_id = Column(String(200), nullable=True)
    
    # Customer information (for gateway)
    customer_name = Column(String(200), nullable=True)
    customer_email = Column(String(255), nullable=True)
    customer_phone = Column(String(20), nullable=True)
    customer_document = Column(String(20), nullable=True)  # CPF/CNPJ
    
    # Billing address
    billing_address_line1 = Column(String(255), nullable=True)
    billing_address_line2 = Column(String(255), nullable=True)
    billing_city = Column(String(100), nullable=True)
    billing_state = Column(String(100), nullable=True)
    billing_postal_code = Column(String(20), nullable=True)
    
    # Fraud detection
    risk_score = Column(Integer, nullable=True)  # 0-100
    fraud_analysis = Column(Text, nullable=True)  # JSON with fraud analysis
    
    # Webhook tracking
    webhook_attempts = Column(Integer, default=0, nullable=False)
    last_webhook_at = Column(DateTime(timezone=True), nullable=True)
    webhook_status = Column(String(50), nullable=True)
    
    # System metadata
    metadata = Column(Text, nullable=True)  # JSON for additional data
    notes = Column(Text, nullable=True)     # Admin notes
    
    # Timestamps
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), onupdate=func.now(), nullable=True)
    
    # Relationships
    order = relationship("Order", back_populates="payment")
    
    def __repr__(self):
        return f"<Payment(id={self.id}, order_id={self.order_id}, status={self.status})>"
    
    @property
    def amount_brl(self) -> float:
        """Get amount in BRL (converting from cents)"""
        return self.amount_cents / 100
    
    @property
    def gateway_fee_brl(self) -> float:
        """Get gateway fee in BRL"""
        return self.gateway_fee_cents / 100
    
    @property
    def platform_fee_brl(self) -> float:
        """Get platform fee in BRL"""
        return self.platform_fee_cents / 100
    
    @property
    def net_amount_brl(self) -> float:
        """Get net amount in BRL"""
        return (self.net_amount_cents or 0) / 100
    
    @property
    def refund_amount_brl(self) -> float:
        """Get refund amount in BRL"""
        return self.refund_amount_cents / 100
    
    @property
    def is_pending(self) -> bool:
        """Check if payment is pending"""
        return self.status in [PaymentStatus.PENDING, PaymentStatus.PROCESSING]
    
    @property
    def is_completed(self) -> bool:
        """Check if payment is successfully completed"""
        return self.status == PaymentStatus.COMPLETED
    
    @property
    def is_failed(self) -> bool:
        """Check if payment failed"""
        return self.status in [PaymentStatus.FAILED, PaymentStatus.CANCELLED]
    
    def to_dict(self, include_sensitive: bool = False) -> dict:
        """Convert payment to dictionary"""
        data = {
            "id": self.id,
            "order_id": self.order_id,
            "method": self.method.value,
            "status": self.status.value,
            "amount_brl": self.amount_brl,
            "currency": self.currency,
            "gateway": self.gateway,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "completed_at": self.completed_at.isoformat() if self.completed_at else None,
        }
        
        if include_sensitive:
            data.update({
                "gateway_transaction_id": self.gateway_transaction_id,
                "pix_code": self.pix_code,
                "pix_qr_code": self.pix_qr_code,
                "pix_expiration": self.pix_expiration.isoformat() if self.pix_expiration else None,
                "gateway_fee_brl": self.gateway_fee_brl,
                "platform_fee_brl": self.platform_fee_brl,
                "net_amount_brl": self.net_amount_brl,
            })
        
        return data