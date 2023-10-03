from abc import ABC, abstractmethod

from domain.entities import AuthToken


class GetFreshToken(ABC):
    @abstractmethod
    async def get(self) -> AuthToken:
        """Abstract method to get a fresh token"""
        raise NotImplementedError()
