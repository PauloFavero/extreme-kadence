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
    space: Optional[KadenceSpace] = Field(alias="space", default=None)
    start_date: Optional[datetime] = Field(alias="startDate", default=None)
    end_date: Optional[datetime] = Field(alias="endDate", default=None)
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")

    checked_in_date: Optional[datetime] = Field(alias="checkedInDate", default=None)
    checked_in_source: CheckInOutSource = Field(
        alias="checkedInSource", default=CheckInOutSource.UNKNOWN
    )
    check_in_method: Optional[CheckInOutMethod] = Field(
        alias="checkInMethod", default=None
    )

    check_out_source: CheckInOutSource = Field(
        alias="checkOutSource", default=CheckInOutSource.UNKNOWN
    )
    check_out_method: Optional[CheckInOutMethod] = Field(
        alias="checkOutMethod", default=None
    )
    checked_out_date: Optional[datetime] = Field(alias="checkedOutDate", default=None)

    cancellation_reason: Optional[CancellationReason] = Field(
        alias="cancellationReason", default=None
    )
    cancelled_date: Optional[datetime] = Field(alias="cancelledDate", default=None)

    permanent: bool = Field(alias="permanent")
    has_guests: bool = Field(alias="hasGuests")
    guest_booking: bool = Field(alias="guestBooking")
    recurring_booking: bool = Field(alias="recurringBooking")
    self_certify_source: CheckInOutSource = Field(
        alias="selfCertifySource", default=CheckInOutSource.UNKNOWN
    )
    source: CheckInOutSource = Field(alias="source", default=CheckInOutSource.UNKNOWN)
    status: BookingStatus = Field(alias="status")
    type: BookingType = Field(alias="type")
    building: Optional[str] = Field(alias="building")

    class Config:
        """Config for Booking Model"""

        json_encoders = {
            datetime: lambda v: v.isoformat(),
        }
