from http import HTTPStatus
from typing import Optional

import requests

from data.protocols import GetKadenceUserHttp
from data.models import KadenceAuthToken, KadenceUser
from config.kadence import KadenceSettings


class KadenceGetUserHttpAdapter(GetKadenceUserHttp):
    """Adapter to get user from Kadence API"""

    def __init__(self, config: KadenceSettings) -> None:
        super().__init__()
        self.__session = requests.Session()
        self.__config = config

    async def get_kadence_user(
        self, token: KadenceAuthToken, user_email: str
    ) -> Optional[KadenceUser]:
        response = self.__session.get(
            f"{self.__config.base_uri}{self.__config.api_version}/users?email={user_email}",
            headers={"Authorization": f"{token.token_type} {token.access_token}"},
        )

        if response.status_code == HTTPStatus.OK:
            data = response.json()
            total = data.get("hydra:totalItems", 0)
            users = data.get("hydra:member", [])
            if total == 1:
                return KadenceUser(**users[0])
            if total > 1:
                raise Exception("More than one user found", users)

        return None
