from typing import Union
from http import HTTPStatus

import requests
from config.kadence import KadenceSettings
from domain.entities.kadence.auth import (
    KadenceAuthError,
    KadenceAuthToken,
    KadenceAuthTokenBodyReq,
)
from domain.protocols.kadence import AuthenticationHttpProtocol


class KadenceAuthRequester(AuthenticationHttpProtocol):
    def __init__(self, config: KadenceSettings) -> None:
        super().__init__()
        self.__session = requests.Session()
        self.__config = config

    async def get_token(self) -> Union[KadenceAuthToken, KadenceAuthError]:
        body_req = KadenceAuthTokenBodyReq(
            client_id=self.__config.identifier, client_secret=self.__config.secret
        )

        response = self.__session.post(
            url=self.__config.login_endpoint, data=body_req.model_dump()
        )

        if response.status_code == HTTPStatus.OK:
            return KadenceAuthToken(**response.json())

        return KadenceAuthError(**response.json())
