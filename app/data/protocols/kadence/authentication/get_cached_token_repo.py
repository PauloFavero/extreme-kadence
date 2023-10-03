from abc import ABC, abstractmethod
from typing import Optional

from data.models import KadenceAuthToken


class GetCachedTokenRepo(ABC):
    """Get cached token repository"""

    @abstractmethod
    async def get(self) -> Optional[KadenceAuthToken]:
        """Abstract method for getting a cached token from the database"""
        raise NotImplementedError()
