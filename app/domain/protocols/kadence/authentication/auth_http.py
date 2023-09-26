
from abc import ABC, abstractmethod
from typing import Union

from domain.entities.http import HttpResponse
from domain.entities.kadence.auth import KadenceAuthError
from domain.entities.kadence import KadenceAuthToken

class AuthenticationHttpProtocol(ABC):
    @abstractmethod
    async def get_token(self) -> HttpResponse[Union[KadenceAuthToken, KadenceAuthError]]:
        pass