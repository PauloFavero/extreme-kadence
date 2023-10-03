from datetime import datetime
from pydantic import BaseModel, Field
from typing import List, Optional

from .space import Space
from .check_in_out import CheckInMethod
from enum import Enum


class Booking(BaseModel):
    id: str
    createdUserId: str
    userId: str
    space: Space
    startDate: datetime
    endDate: datetime
    createdAt: datetime
    updatedAt: datetime
    checkedInSource: CheckInMethod
    checkOutSource: CheckInMethod
    permanent: bool
    hasGuests: bool
    guestBooking: bool
    recurringBooking: bool
    selfCertifySource: str
    source: str
    status: str
    type: str
    building: str

    class Config:
        json_encoders = {
            datetime: lambda v: v.isoformat(),
        }


class BookingList(BaseModel):
    itens: List[Booking]


class BookingType(Enum):
    DESK = "desk"
    ROOM = "room"
    ONSITE = "onsite"


class BookingStatus(Enum):
    BOOKED = "booked"
    CHECKEDIN = "checkedIn"
    CHECKEDOUT = "checkedOut"
    COMPLETED = "completed"
    CANCELLED = "cancelled"
    NOCHECKIN = "noCheckIn"


class CancellationReason(Enum):
    BY_USER="byUser"
    BY_USER_IN_BULK="byUserInBulk"
    AUTO_SPACE_RELEASE="autoSpaceRelease"
    PERMANENT_DESK="permanentDesk"
    CHANGE_IN_BUILD_ING_POLICY="changeInBuildingPolicy"
    CHANGE_IN_COMPANY_POLICY="changeInCompanyPolicy"
    REMOVED_FROM_CALENDAR_BY_PROVIDER="removedFromCalendarByProvider"
    REMOVED_FROM_CALENDAR_BY_KADENCE="removedFromCalendarByKadence"
    CALENDAR_SYNC_ERROR="calendarSyncError"
    SPACE_NO_LONGER_AVAILABLE="spaceNoLongerAvailable"
    SPACE_RESTRICTED="spaceRestricted"
    SPACE_NOT_RESTRICTED_ANYMORE="spaceNotRestrictedAnymore"
    USER_DELETED="userDeleted"
    BUILDING_CLOSURE="buildingClosure"


class FetchBookingsFilterParams(BaseModel):
    type: Optional[BookingType] = BookingType.DESK.value
    status: Optional[BookingStatus] = BookingStatus.BOOKED.value
    startDateTime: Optional[datetime] = Field(
        datetime.fromisoformat("2023-09-27T08:00:00+00:00"), alias="startDateTime[local_strictly_after]"
    )
    # endDateTime: Optional[datetime] = Field(
    #     "2023-09-26T15:00:00+00:00", alias="endDateTime[local_strictly_after]"
    # )
    page: Optional[int] = 1
    itemsPerPage: Optional[int] = 10

