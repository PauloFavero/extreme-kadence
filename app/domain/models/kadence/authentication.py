"""Kadence Domain Models"""

from pydantic import BaseModel

class KadenceAuthTokenBodyReq(BaseModel):
    client_id: str
    grant_type: str = "client_credentials"
    client_secret: str
    scope: str = "public"

class KadenceAuthToken(BaseModel):
    token_type: str
    expires_in: int
    access_token: str

class KadenceAuthError(BaseModel):
    error: str
    error_description: str
    message: str

class KadenceRateLimit(BaseModel):
    x_rate_limit_limit: int # The amount of API requests that can be made by an application / developer per hour.
    x_rate_limit_remaining: int # The amount of API requests that remain for the time window.
    x_rate_limit_retry_after: int # A unix timestamp when the rate limiting will no longer be applied.
