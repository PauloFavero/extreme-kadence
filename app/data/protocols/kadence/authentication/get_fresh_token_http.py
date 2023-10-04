from abc import ABC, abstractmethod

from data.models import KadenceAuthToken, KadenceAuthError


class GetFreshTokenHttp(ABC):
    """Get fresh token use case"""

    @abstractmethod
    async def get(self) -> KadenceAuthToken | KadenceAuthError:
        """Abstract method to get a fresh token from an API"""
        raise NotImplementedError()
