from abc import ABC, abstractmethod
from typing import Optional
from domain.entities import AuthToken, User


class GetUser(ABC):
    """Get user use case"""

    @abstractmethod
    async def get_user(self, token: AuthToken, user_email: str) -> Optional[User]:
        """Get user by email"""
        raise NotImplementedError
