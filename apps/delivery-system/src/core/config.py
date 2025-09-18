"""
Core configuration module for Pyloto Delivery System
Handles environment variables and application settings
"""
from pydantic_settings import BaseSettings
from pydantic import Field, validator
from typing import List, Optional
import secrets
import os


class Settings(BaseSettings):
    """Application settings loaded from environment variables"""
    
    # Application
    APP_NAME: str = "Pyloto Delivery System"
    VERSION: str = "1.0.0"
    DEBUG: bool = Field(default=False, env="DEBUG")
    ENVIRONMENT: str = Field(default="development", env="ENVIRONMENT")
    
    # Security
    SECRET_KEY: str = Field(default_factory=lambda: secrets.token_urlsafe(32))
    JWT_SECRET_KEY: str = Field(default_factory=lambda: secrets.token_urlsafe(32))
    JWT_ALGORITHM: str = "HS256"
    JWT_EXPIRE_MINUTES: int = 60 * 24 * 7  # 7 days
    
    # CORS
    ALLOWED_HOSTS: List[str] = Field(default=["*"])
    CORS_ORIGINS: List[str] = Field(default=["http://localhost:3000", "http://localhost:3001"])
    
    # Database
    DATABASE_URL: str = Field(
        default="postgresql+asyncpg://pyloto:pyloto123@localhost:5432/pyloto_dev",
        env="DATABASE_URL"
    )
    DATABASE_POOL_SIZE: int = Field(default=10, env="DATABASE_POOL_SIZE")
    DATABASE_MAX_OVERFLOW: int = Field(default=20, env="DATABASE_MAX_OVERFLOW")
    
    # Redis
    REDIS_URL: str = Field(default="redis://localhost:6379/0", env="REDIS_URL")
    REDIS_MAX_CONNECTIONS: int = Field(default=20, env="REDIS_MAX_CONNECTIONS")
    
    # Celery
    CELERY_BROKER_URL: str = Field(default="redis://localhost:6379/1", env="CELERY_BROKER_URL")
    CELERY_RESULT_BACKEND: str = Field(default="redis://localhost:6379/2", env="CELERY_RESULT_BACKEND")
    
    # External APIs
    GOOGLE_MAPS_API_KEY: Optional[str] = Field(default=None, env="GOOGLE_MAPS_API_KEY")
    GOOGLE_PLACES_API_KEY: Optional[str] = Field(default=None, env="GOOGLE_PLACES_API_KEY")
    
    WHATSAPP_API_URL: Optional[str] = Field(default=None, env="WHATSAPP_API_URL")
    WHATSAPP_API_TOKEN: Optional[str] = Field(default=None, env="WHATSAPP_API_TOKEN")
    WHATSAPP_PHONE_NUMBER_ID: Optional[str] = Field(default=None, env="WHATSAPP_PHONE_NUMBER_ID")
    
    PAGSEGURO_TOKEN: Optional[str] = Field(default=None, env="PAGSEGURO_TOKEN")
    PAGSEGURO_EMAIL: Optional[str] = Field(default=None, env="PAGSEGURO_EMAIL")
    PAGSEGURO_SANDBOX: bool = Field(default=True, env="PAGSEGURO_SANDBOX")
    
    OPENAI_API_KEY: Optional[str] = Field(default=None, env="OPENAI_API_KEY")
    OPENAI_ASSISTANT_ID: str = Field(default="asst_RGAVvFf5IhLa8tShJ0gZWsYX", env="OPENAI_ASSISTANT_ID")
    OPENAI_MODEL: str = Field(default="gpt-4", env="OPENAI_MODEL")
    
    # Monitoring
    SENTRY_DSN: Optional[str] = Field(default=None, env="SENTRY_DSN")
    LOG_LEVEL: str = Field(default="INFO", env="LOG_LEVEL")
    
    # File Storage
    UPLOAD_DIR: str = Field(default="./data/uploads", env="UPLOAD_DIR")
    MAX_FILE_SIZE: int = Field(default=10 * 1024 * 1024, env="MAX_FILE_SIZE")  # 10MB
    
    # Rate Limiting
    RATE_LIMIT_REQUESTS: int = Field(default=100, env="RATE_LIMIT_REQUESTS")
    RATE_LIMIT_WINDOW: int = Field(default=60, env="RATE_LIMIT_WINDOW")  # seconds
    
    # Business Logic
    DEFAULT_DELIVERY_RADIUS_KM: float = Field(default=20.0, env="DEFAULT_DELIVERY_RADIUS_KM")
    MIN_DELIVERY_PRICE: float = Field(default=5.0, env="MIN_DELIVERY_PRICE")
    MAX_DELIVERY_PRICE: float = Field(default=100.0, env="MAX_DELIVERY_PRICE")
    DELIVERY_FEE_PER_KM: float = Field(default=2.5, env="DELIVERY_FEE_PER_KM")
    
    @validator("ALLOWED_HOSTS", pre=True)
    def parse_allowed_hosts(cls, v):
        if isinstance(v, str):
            return [host.strip() for host in v.split(",")]
        return v
    
    @validator("CORS_ORIGINS", pre=True)
    def parse_cors_origins(cls, v):
        if isinstance(v, str):
            return [origin.strip() for origin in v.split(",")]
        return v
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = True


# Global settings instance
settings = Settings()


# Environment-specific configurations
def get_database_url() -> str:
    """Get database URL based on environment"""
    if settings.ENVIRONMENT == "test":
        return settings.DATABASE_URL.replace("/pyloto_dev", "/pyloto_test")
    return settings.DATABASE_URL


def is_development() -> bool:
    """Check if running in development mode"""
    return settings.ENVIRONMENT == "development" or settings.DEBUG


def is_production() -> bool:
    """Check if running in production mode"""
    return settings.ENVIRONMENT == "production"


def is_testing() -> bool:
    """Check if running in test mode"""
    return settings.ENVIRONMENT == "test"