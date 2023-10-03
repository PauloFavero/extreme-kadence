
from abc import ABC, abstractmethod

from data.models import KadenceAuthToken

class GetCachedTokenRepo(ABC):
  
    @abstractmethod
    async def get(self) -> KadenceAuthToken:
        """Abstract method for getting a cached token from the database"""
        raise NotImplementedError()