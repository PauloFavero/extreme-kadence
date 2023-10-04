from pydantic import AliasChoices, Field
from pydantic_settings import BaseSettings


class SentrySettings(BaseSettings):
    """Sentry Settings"""

    dsn: str = Field(
        "",
        alias=AliasChoices("sentry_dsn", "sentry_url"),
    )
    traces_sample_rate: float = Field(1.0, alias="sentry_traces_sample_rate")
    sample_rate: float = Field(1.0, alias="sentry_sample_rate")
    env: str = Field("production", alias="sentry_env")
    release: str = Field("1.0.0", alias="api_version")
