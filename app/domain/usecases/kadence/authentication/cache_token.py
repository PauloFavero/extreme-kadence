from abc import ABC, abstractmethod

from domain.entities import AuthToken


class CacheToken(ABC):
    @abstractmethod
    def cache(self, token: AuthToken) -> None:
        """Abstract method to cache token"""
        raise NotImplementedError()
