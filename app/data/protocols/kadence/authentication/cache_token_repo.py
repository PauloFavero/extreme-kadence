from abc import ABC, abstractmethod

from data.models import KadenceAuthToken


class CacheTokenRepo(ABC):
    """Cache token repository"""

    @abstractmethod
    async def persist(self, token: KadenceAuthToken) -> None:
        """Abstract method to cache a token in the database"""
        raise NotImplementedError()
