from abc import ABC, abstractmethod

from data.models import KadenceAuthToken, KadenceAuthError


class GetFreshTokenHttp(ABC):
    @abstractmethod
    async def get(self) -> KadenceAuthToken | KadenceAuthError:
        """Abstract method to get a fresh token from an API"""
        raise NotImplementedError()
