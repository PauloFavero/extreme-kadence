from datetime import datetime
from abc import ABC, abstractmethod
from typing import Optional, List

from pydantic import BaseModel, Field

from domain.entities import BookingStatus, BookingType
from data.models import (
    KadenceBooking,
    KadenceAuthToken,
)


class KadenceGetBookingsQueryParams(BaseModel):
    """Get Bookings Filter Params Model"""

    type: Optional[BookingType] = BookingType.DESK
    status: Optional[BookingStatus] = BookingStatus.NO_CHECKIN
    start_date: Optional[datetime] = Field(
        alias="startDateTime[local_strictly_after]", default=None
    )
    end_date: Optional[datetime] = Field(
        alias="endDateTime[local_strictly_after]", default=None
    )
    page: Optional[int] = 1
    items_per_page: Optional[int] = Field(alias="itemsPerPage", default=10)

    class Config:  # pylint: disable=missing-class-docstring
        use_enum_values = True
        validate_default = True


class GetUserBookingsHttp(ABC):
    """Data Protocol to Get User Bookings"""

    @abstractmethod
    def get_bookings_by_user_id(
        self,
        token: KadenceAuthToken,
        user_id: str,
        query_params: Optional[KadenceGetBookingsQueryParams] = None,
    ) -> List[KadenceBooking]:
        """Abstract method to get bookings by user id"""
        raise NotImplementedError("Method not implemented")
