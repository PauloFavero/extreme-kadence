from http import HTTPStatus

from config.kadence import KadenceSettings
from data.models import KadenceAuthError, KadenceAuthToken
from data.protocols import GetFreshTokenHttp

import requests
from pydantic import BaseModel


class KadenceAuthTokenBodyReq(BaseModel):
    """Kadence Auth Token Body Request Model"""

    client_id: str
    grant_type: str = "client_credentials"
    client_secret: str
    scope: str = "public"


class KadenceFreshTokenHttpAdapter(GetFreshTokenHttp):
    """Class to request a new token from Kadence API."""

    def __init__(self, config: KadenceSettings) -> None:
        super().__init__()
        self.__session = requests.Session()
        self.__config = config

    async def get(self) -> KadenceAuthToken | KadenceAuthError:
        """Get a new authentication token from Kadence API."""
        body_req = KadenceAuthTokenBodyReq(
            client_id=self.__config.identifier, client_secret=self.__config.secret
        )

        response = self.__session.post(
            url=self.__config.login_endpoint, data=body_req.model_dump()
        )

        if response.status_code == HTTPStatus.OK:
            return KadenceAuthToken(**response.json())

        return KadenceAuthError(**response.json())
