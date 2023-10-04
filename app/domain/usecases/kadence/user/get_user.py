from abc import ABC, abstractmethod
from domain.entities import AuthToken, User


class GetUser(ABC):
    """Get user use case"""

    @abstractmethod
    def get_user(self, token: AuthToken, user_email: str) -> User:
        """Get user by email"""
        raise NotImplementedError
