from typing import Optional
from abc import ABC, abstractmethod

from data.models import KadenceBooking


class GetBookingByIdHttpProtocol(ABC):
    @abstractmethod
    def get_booking_by_id(self, booking_id: str) -> Optional[KadenceBooking]:
        """Abstract method to get booking by id"""
        raise NotImplementedError("Method not implemented")
