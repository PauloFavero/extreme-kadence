from datetime import datetime
from pydantic import BaseModel, Field
from typing import List, Optional

from domain.entities.kadence.check_in_out import CheckInMethod
from domain.entities.kadence.space import Space
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
    BYUSER="byUser"
    BYUSERINBULK="byUserInBulk"
    AUTOSPACERELEASE="autoSpaceRelease"
    PERMANENTDESK="permanentDesk"
    CHANGEINBUILDINGPOLICY="changeInBuildingPolicy"
    CHANGEINCOMPANYPOLICY="changeInCompanyPolicy"
    REMOVEDFROMCALENDARBYPROVIDER="removedFromCalendarByProvider"
    REMOVEDFROMCALENDARBYKADENCE="removedFromCalendarByKadence"
    CALENDARSYNCERROR="calendarSyncError"
    SPACENOLONGERAVAILABLE="spaceNoLongerAvailable"
    SPACERESTRICTED="spaceRestricted"
    SPACENOTRESTRICTEDANYMORE="spaceNotRestrictedAnymore"
    USERDELETED="userDeleted"
    BUILDINGCLOSURE="buildingClosure"

#    "startDate": "2023-09-26T08:00:00+00:00",
#     "endDate": "2023-09-26T16:00:00+00:00",

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

