import redis
import json
from app.core.config import settings

class RedisClient:
    def __init__(self):
        self.client = redis.Redis(
            host=settings.REDIS_HOST,
            port=settings.REDIS_PORT,
            password=settings.REDIS_PASSWORD,
            decode_responses=True
        )

    def get_json(self, key):
        data = self.client.get(key)
        return json.loads(data) if data else None

    def set_with_ttl(self, key, value, ttl=None):
        self.client.set(key, value, ex=ttl)

    def delete(self, key):
        self.client.delete(key)

redis_client = RedisClient()

def get_redis():
    return redis_client
