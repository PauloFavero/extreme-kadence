"""Redis Singleton

This module implements a singleton class for Redis connections.

The Redis is used to store the access token and refresh token of the
Kadence API.

"""

import os

import redis


class RedisSingleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            host = os.getenv("REDIS_HOST", "localhost")
            port = int(os.getenv("REDIS_PORT", 6379))
            db = int(os.getenv("REDIS_DB", 0))

            cls._instance = super(RedisSingleton, cls).__new__(cls)
            cls._instance.initialize_redis_connection(host, port, db)
        return cls._instance

    def initialize_redis_connection(self, host, port, db):
        self.redis_client = redis.StrictRedis(host=host, port=port, db=db)

    def set(self, key, value, ex=None):
        return self.redis_client.set(key, value, ex=ex)

    def get(self, key):
        return self.redis_client.get(key)

    def delete(self, key):
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
