from abc import ABC, abstractmethod

from domain.entities import AuthToken


class CacheToken(ABC):
    """Cache token use case"""

    @abstractmethod
    def cache(self, token: AuthToken) -> None:
        """Abstract method to cache token"""
        raise NotImplementedError()
