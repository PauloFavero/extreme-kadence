from abc import ABC, abstractmethod
from typing import Any


class AuthMiddleware(ABC):
    """Abstract class to act as a middleware for authentication"""

    @abstractmethod
    async def handle(self) -> Any:
        """Abstract method to act as a middleware for authentication"""
        raise NotImplementedError
