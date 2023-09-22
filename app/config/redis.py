from pydantic import (
    AliasChoices,
    Field
)
from pydantic_settings import BaseSettings

class RedisSettings(BaseSettings):
    host: str = Field(
        "cache", validation_alias=AliasChoices("redis_dsn", "redis_url")
    )
    port: int = Field(6379, alias="redis_port")
    db: int = Field(0, alias="redis_db")
