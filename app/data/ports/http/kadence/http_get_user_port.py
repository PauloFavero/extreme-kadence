from typing import Optional
from domain.usecases import GetUser
from domain.entities import AuthToken, User

from data.models import KadenceAuthToken
from data.protocols import GetKadenceUserHttp


class KadenceGetUserHttpPort(GetUser):
    """Class representing the KadenceGetUserHttpPort"""

    def __init__(self, adapter: GetKadenceUserHttp) -> None:
        self._adapter = adapter

    async def get_user(self, token: AuthToken, user_email: str) -> Optional[User]:
        """Get user by email"""
        kdc_token = KadenceAuthToken(
            access_token=token.token,
            token_type=token.type,
            expires_at=token.expire_at,
            expires_in=token.expire_in,
        )
        kdc_user = await self._adapter.get_kadence_user(
            token=kdc_token, user_email=user_email
        )
        if kdc_user is None:
            return None

        return User(
            id=kdc_user.id,
            email=kdc_user.email,
            first_name=kdc_user.first_name,
            last_name=kdc_user.last_name,
        )
