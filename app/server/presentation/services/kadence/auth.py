from http import HTTPStatus
from typing import Optional, Union

from fastapi import HTTPException
from domain.entities import AuthToken
from domain.usecases import CacheToken, GetCachedToken, GetFreshToken


class KadenceAuthService:
    """Kadence authentication service"""

    def __init__(
        self,
        cache_port: Union[GetCachedToken, CacheToken],
        http_port: GetFreshToken,
    ) -> None:
        self.cache_port = cache_port
        self.http_port = http_port

    async def handle(self) -> Optional[AuthToken]:
        """Method to handle authentication"""
        try:
            cached_token = self.cache_port.get()

            if cached_token:
                return cached_token
            else:
                fresh_token = await self.http_port.get()
                self.cache_port.cache(fresh_token)

                return fresh_token

        except Exception as error:
            print("Error while fetching Kadence fresh_token: ", error)
            raise HTTPException(
                status_code=HTTPStatus.UNAUTHORIZED, detail=error.__str__()
            ) from error
