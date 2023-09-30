"""Kadence Domain Models"""
from time import time
from typing import Any

from pydantic import BaseModel, model_validator, root_validator


class KadenceAuthTokenBodyReq(BaseModel):
    client_id: str
    grant_type: str = "client_credentials"
    client_secret: str
    scope: str = "public"


class KadenceAuthToken(BaseModel):
    token_type: str
    expires_in: int
    access_token: str
    expires_at: int

    @model_validator(mode="before")
    @classmethod
    def check_card_number_omitted(cls, data: Any) -> Any:
        if isinstance(data, dict):
            exp_at: int = data.get("expires_at", None)
            if exp_at is None:
                exp_in: int = data.get("expires_in", 0)
                data["expires_at"] = int(exp_in) + int(time())
        return data


class KadenceAuthError(BaseModel):
    error: str
    error_description: str
    message: str


class KadenceRateLimit(BaseModel):
    x_rate_limit_limit: int  # The amount of API requests that can be made by an application / developer per hour.
    x_rate_limit_remaining: int  # The amount of API requests that remain for the time window.
    x_rate_limit_retry_after: int  # A unix timestamp when the rate limiting will no longer be applied.
