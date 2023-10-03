from abc import ABC, abstractmethod
from typing import Optional, Tuple
from data.models import (
    BookingList,
    HydraPagination,
    KadenceAuthToken,
    FetchBookingsFilterParams,
)


class GetUserBookingsHttpProtocol(ABC):
    @abstractmethod
    def get_bookings_by_user_id(
        self,
        user_id: str,
        token: KadenceAuthToken,
        filter: Optional[FetchBookingsFilterParams] = None,
    ) -> Tuple[BookingList, Optional[HydraPagination]]:
        """Abstract method to get bookings by user id"""
        raise NotImplementedError("Method not implemented")

    @abstractmethod
    def get_bookings_from_pagination(
        self,
        pagination: HydraPagination,
        token: KadenceAuthToken,
    ) -> Tuple[BookingList, Optional[HydraPagination]]:
        """Abstract method to get bookings by user id"""
        raise NotImplementedError("Method not implemented")
