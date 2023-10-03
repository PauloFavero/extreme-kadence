from pydantic import BaseModel


class AuthToken(BaseModel):
    """Authentication token."""

    token: str
    type: str
