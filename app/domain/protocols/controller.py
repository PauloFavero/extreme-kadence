from abc import ABC, abstractmethod
from typing import Any


class Controller(ABC):
    @abstractmethod
    async def handle(self, request: Any = None) -> Any:
        """Abstract method for handle a request and return a response"""
        raise NotImplementedError
    