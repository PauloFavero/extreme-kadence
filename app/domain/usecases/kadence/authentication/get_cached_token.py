from abc import ABC, abstractmethod
from typing import Optional

from domain.entities import AuthToken


class GetCachedToken(ABC):
    """Get cached token use case"""

    @abstractmethod
    def get(self) -> Optional[AuthToken]:
        """Abstract method to get a cached token by prefix"""
        raise NotImplementedError()
