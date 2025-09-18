"""
Redis cache configuration and connection management
"""
import redis.asyncio as redis
import json
import pickle
from typing import Any, Optional, Dict, Union
import logging
from datetime import timedelta

from .config import settings

logger = logging.getLogger(__name__)

# Redis connection pool
redis_pool: Optional[redis.ConnectionPool] = None
redis_client: Optional[redis.Redis] = None


async def init_redis():
    """Initialize Redis connection"""
    global redis_pool, redis_client
    
    try:
        redis_pool = redis.ConnectionPool.from_url(
            settings.REDIS_URL,
            max_connections=settings.REDIS_MAX_CONNECTIONS,
            decode_responses=True,
            encoding="utf-8"
        )
        
        redis_client = redis.Redis(connection_pool=redis_pool)
        
        # Test connection
        await redis_client.ping()
        logger.info("Redis connection established successfully")
        
    except Exception as e:
        logger.error(f"Error connecting to Redis: {e}")
        raise


async def get_redis() -> redis.Redis:
    """Get Redis client instance"""
    if redis_client is None:
        await init_redis()
    return redis_client


class CacheManager:
    """Cache manager for handling different types of data"""
    
    def __init__(self):
        self.redis_client = None
    
    async def _get_client(self) -> redis.Redis:
        """Get Redis client"""
        if self.redis_client is None:
            self.redis_client = await get_redis()
        return self.redis_client
    
    async def set(
        self,
        key: str,
        value: Any,
        expire: Optional[Union[int, timedelta]] = None,
        serialize: str = "json"
    ) -> bool:
        """
        Set a value in cache
        
        Args:
            key: Cache key
            value: Value to cache
            expire: Expiration time in seconds or timedelta
            serialize: Serialization method ('json' or 'pickle')
        """
        try:
            client = await self._get_client()
            
            # Serialize value
            if serialize == "json":
                serialized_value = json.dumps(value, default=str)
            elif serialize == "pickle":
                serialized_value = pickle.dumps(value)
            else:
                serialized_value = str(value)
            
            # Set expiration
            if isinstance(expire, timedelta):
                expire = int(expire.total_seconds())
            
            await client.set(key, serialized_value, ex=expire)
            return True
            
        except Exception as e:
            logger.error(f"Error setting cache key {key}: {e}")
            return False
    
    async def get(
        self,
        key: str,
        default: Any = None,
        serialize: str = "json"
    ) -> Any:
        """
        Get a value from cache
        
        Args:
            key: Cache key
            default: Default value if key not found
            serialize: Serialization method used when setting
        """
        try:
            client = await self._get_client()
            value = await client.get(key)
            
            if value is None:
                return default
            
            # Deserialize value
            if serialize == "json":
                return json.loads(value)
            elif serialize == "pickle":
                return pickle.loads(value)
            else:
                return value
                
        except Exception as e:
            logger.error(f"Error getting cache key {key}: {e}")
            return default
    
    async def delete(self, key: str) -> bool:
        """Delete a key from cache"""
        try:
            client = await self._get_client()
            result = await client.delete(key)
            return bool(result)
        except Exception as e:
            logger.error(f"Error deleting cache key {key}: {e}")
            return False
    
    async def exists(self, key: str) -> bool:
        """Check if key exists in cache"""
        try:
            client = await self._get_client()
            result = await client.exists(key)
            return bool(result)
        except Exception as e:
            logger.error(f"Error checking cache key {key}: {e}")
            return False
    
    async def increment(self, key: str, amount: int = 1) -> Optional[int]:
        """Increment a numeric value in cache"""
        try:
            client = await self._get_client()
            result = await client.incrby(key, amount)
            return result
        except Exception as e:
            logger.error(f"Error incrementing cache key {key}: {e}")
            return None
    
    async def expire(self, key: str, seconds: int) -> bool:
        """Set expiration time for a key"""
        try:
            client = await self._get_client()
            result = await client.expire(key, seconds)
            return bool(result)
        except Exception as e:
            logger.error(f"Error setting expiration for cache key {key}: {e}")
            return False
    
    async def clear_pattern(self, pattern: str) -> int:
        """Clear all keys matching a pattern"""
        try:
            client = await self._get_client()
            keys = await client.keys(pattern)
            if keys:
                result = await client.delete(*keys)
                return result
            return 0
        except Exception as e:
            logger.error(f"Error clearing cache pattern {pattern}: {e}")
            return 0


# Global cache manager instance
cache = CacheManager()


# Session storage for user sessions
class SessionManager:
    """Manage user sessions in Redis"""
    
    def __init__(self, prefix: str = "session:"):
        self.prefix = prefix
        self.default_expire = 60 * 60 * 24 * 7  # 7 days
    
    async def create_session(self, user_id: str, data: Dict[str, Any]) -> str:
        """Create a new session"""
        import uuid
        session_id = str(uuid.uuid4())
        session_key = f"{self.prefix}{session_id}"
        
        session_data = {
            "user_id": user_id,
            "created_at": str(datetime.utcnow()),
            **data
        }
        
        await cache.set(session_key, session_data, expire=self.default_expire)
        return session_id
    
    async def get_session(self, session_id: str) -> Optional[Dict[str, Any]]:
        """Get session data"""
        session_key = f"{self.prefix}{session_id}"
        return await cache.get(session_key)
    
    async def update_session(self, session_id: str, data: Dict[str, Any]) -> bool:
        """Update session data"""
        session_key = f"{self.prefix}{session_id}"
        existing_data = await self.get_session(session_id)
        
        if existing_data:
            existing_data.update(data)
            return await cache.set(session_key, existing_data, expire=self.default_expire)
        return False
    
    async def delete_session(self, session_id: str) -> bool:
        """Delete a session"""
        session_key = f"{self.prefix}{session_id}"
        return await cache.delete(session_key)


# Global session manager
session_manager = SessionManager()


# Health check function
async def check_redis_health() -> bool:
    """Check if Redis is healthy"""
    try:
        client = await get_redis()
        await client.ping()
        return True
    except Exception as e:
        logger.error(f"Redis health check failed: {e}")
        return False