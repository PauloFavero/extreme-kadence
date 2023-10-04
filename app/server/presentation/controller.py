from abc import ABC, abstractmethod
from typing import Any, Optional


class Controller(ABC):
    @abstractmethod
    async def handle(self, request: Optional[Any] = None) -> Any:
        """Abstract method for handle a request and return a response"""
        raise NotImplementedError
