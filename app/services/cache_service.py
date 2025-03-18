import json
import os
from functools import wraps
from typing import Callable

import redis

redis_client = redis.Redis.from_url(os.getenv("REDIS_URL"))


def cache_response(ttl: int = 3600):
    def decorator(func: Callable):
        @wraps(func)
        def wrapper(*args, **kwargs):
            cache_key = f"{func.__name__}:{str(args)}:{str(kwargs)}"
            cached_result = redis_client.get(cache_key)
            if cached_result:
                return json.loads(cached_result)

            result = func(*args, **kwargs)
            redis_client.set(cache_key, json.dumps(result), ex=ttl)
            return result

        return wrapper

    return decorator
