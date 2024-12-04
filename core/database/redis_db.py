import os
import redis

__all__ = ["redis_client"]

redis_client_instance = None


def redis_client() -> redis.Redis:
    global redis_client_instance
    if not redis_client_instance:
        redis_client_instance = redis.from_url(
            url=os.environ["REDIS_URL"],
            decode_responses=True,
        )
    return redis_client_instance
