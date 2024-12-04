from redis.client import Redis
from core.types import Uploader

__all__ = ["get_redis_uploader"]


def get_redis_uploader(redis_client: Redis, key: str) -> Uploader:
    def uploader(data: str):
        redis_client.set(key, data)
        return data

    return uploader
