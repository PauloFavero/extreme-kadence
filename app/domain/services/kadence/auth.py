from time import time
from http import HTTPStatus
from traceback import print_tb
from typing import Union, Any
from pydantic import InstanceOf

import requests
from config.kadence import KadenceSettings
from domain.protocols.controller import Controller
from domain.protocols.kadence.auth_http import AuthenticationHttpProtocol
from domain.protocols.kadence.auth_repo import AuthenticationRepoProtocol

from domain.entities.kadence import (
    KadenceAuthToken,
    KadenceAuthError,
)

class KadenceAuthService(Controller):
    def __init__(self, 
                 repo: AuthenticationRepoProtocol, 
                 requester: AuthenticationHttpProtocol, 
                 config: KadenceSettings) -> None:
        self.repo = repo
        self.requester = requester
        self.config = config

    def __validate_token_expiration(self, token: KadenceAuthToken) -> bool:
        curr_time = int(time())
        expires_in = int(token.expires_in)
        if curr_time < expires_in:
            return True

        return False

    async def handle(self, request: Any = None) -> Union[KadenceAuthToken, 
                                                        KadenceAuthError, 
                                                        None]:
        cached_token = await self.repo.get_cached_token()

        if cached_token and self.__validate_token_expiration(cached_token):
            return cached_token

        else:
            token = await self.requester.get_token()
            
            if isinstance(token, KadenceAuthToken):
                self.repo.persist(token)
            else:
                print(
                    "Error while fetching Kadence token: ", token
                )
                self.repo.delete()
            return token
