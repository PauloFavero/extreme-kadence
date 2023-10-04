"""Kadence Domain Models"""
from time import time
from typing import Any, Optional

from pydantic import BaseModel, model_validator


class KadenceAuthToken(BaseModel):
    """Kadence Auth Token Model"""

    token_type: str
    expires_in: int
    access_token: str
    expires_at: int

    @model_validator(mode="before")
    @classmethod
    def check_card_number_omitted(cls, data: Any) -> Any:
        """Method to validate and build expires_at field"""
        if isinstance(data, dict):
            exp_at: Optional[int] = data.get("expires_at", None)
            if exp_at is None:
                exp_in: int = data.get("expires_in", 0)
                data["expires_at"] = int(exp_in) + int(time())
        return data


class KadenceAuthError(BaseModel):
    """Kadence Auth Error Model"""

    error: str
    error_description: str
    message: str


class KadenceRateLimit(BaseModel):
    """Kadence Rate Limit Model"""

    x_rate_limit_limit: int  # The amount of API requests that can be made by an application / developer per hour.
    x_rate_limit_remaining: int  # The amount of API requests that remain for the time window.
    x_rate_limit_retry_after: int  # A unix timestamp when the rate limiting will no longer be applied.
