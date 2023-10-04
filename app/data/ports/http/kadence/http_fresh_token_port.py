from data.models import KadenceAuthToken
from domain.entities import AuthToken
from domain.usecases import GetFreshToken
from data.protocols import GetFreshTokenHttp


class KadenceFreshTokenHttpPort(GetFreshToken):
    """Class to define the KadenceFreshTokenHttpPort"""

    def __init__(self, http_adapter: GetFreshTokenHttp):
        self.http_adapter = http_adapter

    async def get(self) -> AuthToken:
        """Method to get an authentication token from the kadence API""" ""
        kadence_token = await self.http_adapter.get()

        if isinstance(kadence_token, KadenceAuthToken):
            return AuthToken(
                token=kadence_token.access_token,
                type=kadence_token.token_type,
                expire_at=kadence_token.expires_at,
                expire_in=kadence_token.expires_in,
            )
        raise Exception(
            "Error on getting kadence authentication token",
            kadence_token.model_dump(),
        )
