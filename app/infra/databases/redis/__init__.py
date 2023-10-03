"""Redis Singleton

This module implements a singleton class for Redis connections.

The Redis is used to store the access token and refresh token of the
Kadence API.

"""
from typing import Any, List
import redis

from config import environment


class RedisSingleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(RedisSingleton, cls).__new__(cls)
            cls._instance.initialize(
                environment.redis.host, environment.redis.port, environment.redis.db
            )
        return cls._instance

    def initialize(self, host, port, db):
        self.redis_client = redis.StrictRedis(
            host=host, port=port, db=db, decode_responses=True
        )

    def set(self, key: str, value: Any, ex: int = None, nx: bool = False):
        return self.redis_client.set(key, value, ex=ex, nx=nx)

    def get(self, key: str):
        return self.redis_client.get(key)

    def getmany(self, keys: List[str]):
        return self.redis_client.mget(*keys)

    def delete(self, key: str):
        return self.redis_client.delete(key)


# Example usage:
if __name__ == "__main__":
    redis_instance_1 = RedisSingleton()
    redis_instance_2 = RedisSingleton()

    # Both instances will point to the same Redis connection
    print(redis_instance_1 is redis_instance_2)  # True

    # You can use the Redis connection through either instance
    redis_instance_1.set("example_key", "example_value")
    value = redis_instance_2.get("example_key")
    print(value)  # 'example_value'
