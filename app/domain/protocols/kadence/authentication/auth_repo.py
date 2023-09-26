
from abc import ABC, abstractmethod
from domain.entities.kadence import KadenceAuthToken

class AuthenticationRepoProtocol(ABC):
    @abstractmethod
    async def delete(self) -> None:
        pass
    
    @abstractmethod
    async def get_cached_token(self) -> KadenceAuthToken:
        pass
    
    @abstractmethod
    async def persist(self, token: KadenceAuthToken) -> None:
        pass