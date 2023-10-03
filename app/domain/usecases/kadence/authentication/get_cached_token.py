from abc import ABC, abstractmethod

from domain.entities import AuthToken


class GetCachedToken(ABC):
    @abstractmethod
    def cache(self, prefix: str) -> AuthToken:
        """Abstract method to get a cached token by prefix"""
        raise NotImplementedError()
