import redis
import sys
from ..import REDIS_PORT,REDIS_HOST

def redis_connect() -> redis.client.Redis:
    try:
        client = redis.Redis(
           
            host=REDIS_HOST,
            # host="127.0.0.1",

            
            port=REDIS_PORT ,
            socket_timeout=5,
        )
        ping = client.ping()
        if ping is True:
            return client
    except redis.AuthenticationError:
        print("AuthenticationError")
        sys.exit(1)



client = redis_connect()