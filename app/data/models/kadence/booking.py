from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field
from .space import KadenceSpace

from domain.entities import (
    BookingStatus,
    BookingType,
    CancellationReason,
    CheckInOutMethod,
    CheckInOutSource,
)


class KadenceBooking(BaseModel):
    """Booking Model"""

    id: str
    created_user_id: Optional[str] = Field(alias="createdUserId")
    user_id: Optional[str] = Field(alias="userId")
    space: Optional[KadenceSpace]
    # start_date: Optional[datetime] = Field(alias="startDate")
    # end_date: Optional[datetime] = Field(alias="endDate")
    # created_at: datetime = Field(alias="createdAt")
    # updated_at: datetime = Field(alias="updatedAt")

    # checked_in_date: Optional[datetime] = Field(alias="checkedInDate")
    # checked_in_source: CheckInOutSource
    # check_in_method: Optional[CheckInOutMethod]

    # check_out_source: CheckInOutSource
    # check_out_method: Optional[CheckInOutMethod]
    # checked_out_date: Optional[datetime] = Field(alias="checkedOutDate")

    # cancellation_reason: Optional[CancellationReason] = Field(
    #     alias="cancellationReason"
    # )
    # cancelled_date: Optional[datetime] = Field(alias="cancelledDate")

    # permanent: bool
    # has_guests: bool
    # guest_booking: bool
    # recurring_booking: bool
    # self_certify_source: str
    # source: CheckInOutSource
    # status: BookingStatus
    # type: BookingType
    # building: Optional[str]

    class Config:
        """Config for Booking Model"""

        json_encoders = {
            datetime: lambda v: v.isoformat(),
        }
