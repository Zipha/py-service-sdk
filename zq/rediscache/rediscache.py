from . redis_setup import client
from . redis_config import cache_seconds
from datetime import datetime, timedelta

def get_routes_from_cache(key: str) -> str:
    """Get data from redis."""

    val = client.get(key)
    return val


def set_routes_to_cache(key: str, value: str) -> bool:
    """Set data to redis."""

    state = client.setex(key, timedelta(seconds=cache_seconds), value=value, )
    return state