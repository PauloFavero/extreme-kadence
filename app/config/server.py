from pydantic import Field
from pydantic_settings import BaseSettings

from .redis import RedisSettings
from .sentry import SentrySettings
from .kadence import KadenceSettings
from .uvicorn import UvicornSettings


class ServerSettings(BaseSettings):
    """Server Settings"""

    uvicorn: UvicornSettings = Field(UvicornSettings())
    redis: RedisSettings = Field(RedisSettings())
    sentry: SentrySettings = Field(SentrySettings())
    kadence: KadenceSettings = Field(KadenceSettings())


environment = ServerSettings()


if __name__ == "__main__":
    print(ServerSettings().model_dump())
