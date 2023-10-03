from abc import ABC, abstractmethod


class GetBookingByIdHttpProtocol(ABC):
    @abstractmethod
    def get_booking_by_id(self, booking_id: str) -> dict:
        """Abstract method to get booking by id"""
        raise NotImplementedError("Method not implemented")
