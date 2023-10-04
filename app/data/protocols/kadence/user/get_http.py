from abc import ABC, abstractmethod
from typing import Optional

from data.models import KadenceAuthToken
from data.models import KadenceUser


class GetKadenceUserHttp(ABC):
    """Get kadence user protocol"""

    @abstractmethod
    async def get_kadence_user(
        self, token: KadenceAuthToken, user_email: str
    ) -> Optional[KadenceUser]:
        """Get kaence user by email"""
        raise NotImplementedError
