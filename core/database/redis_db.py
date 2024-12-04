import os
import redis

__all__ = ["redis_client"]

redis_client_instance = redis.from_url(
    url=os.environ["REDIS_URL"],
    decode_responses=True,
)
redis_client_instance.ping()  # verify connection


def redis_client() -> redis.Redis:
    return redis_client_instance
