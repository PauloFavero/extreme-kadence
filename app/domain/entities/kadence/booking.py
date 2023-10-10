from datetime import datetime
from enum import Enum
from typing import Optional

from pydantic import BaseModel


class CheckInOutMethod(Enum):
    """Check in method."""

    DOOR = "door"
    WIFI = "wifi"
    GEOFENCE = "front_desk"
    SENSOR = "sensor"
    UNKNOWN = "unknown"


class CheckInOutSource(Enum):
    """Check in source."""

    WEB = "web"
    IOS = "ios"
    ANDROID = "android"
    CALENDAR = "calendar"
    PUBLICAPI = "publicApi"
    SLACK = "slack"
    MSTEAMS = "msTeams"
    UNKNOWN = "unknown"


class Neighborhood(BaseModel):
    """Neighborhood Model"""

    id: str
    name: str


class Floor(BaseModel):
    """Floor Model"""

    id: str
    name: str


class SpaceType(Enum):
    """Space type."""

    DESK = "desk"
    ROOM = "room"


class BookingType(Enum):
    """Booking type."""

    DESK = "desk"
    ROOM = "room"
    ONSITE = "onsite"


class BookingStatus(Enum):
    """Booking status."""

    BOOKED = "booked"
    CHECKED_IN = "checkedIn"
    CHECKED_OUT = "checkedOut"
    COMPLETED = "completed"
    CANCELLED = "cancelled"
    NO_CHECKIN = "noCheckIn"


class CancellationReason(Enum):
    """Cancellation reason."""

    BY_USER = "byUser"
    BY_USER_IN_BULK = "byUserInBulk"
    AUTO_SPACE_RELEASE = "autoSpaceRelease"
    PERMANENT_DESK = "permanentDesk"
    CHANGE_IN_BUILD_ING_POLICY = "changeInBuildingPolicy"
    CHANGE_IN_COMPANY_POLICY = "changeInCompanyPolicy"
    REMOVED_FROM_CALENDAR_BY_PROVIDER = "removedFromCalendarByProvider"
    REMOVED_FROM_CALENDAR_BY_KADENCE = "removedFromCalendarByKadence"
    CALENDAR_SYNC_ERROR = "calendarSyncError"
    SPACE_NO_LONGER_AVAILABLE = "spaceNoLongerAvailable"
    SPACE_RESTRICTED = "spaceRestricted"
    SPACE_NOT_RESTRICTED_ANYMORE = "spaceNotRestrictedAnymore"
    USER_DELETED = "userDeleted"
    BUILDING_CLOSURE = "buildingClosure"


class Booking(BaseModel):
    """Booking Entity"""

    id: str
    user_id: Optional[str]
    start_date: Optional[datetime]
    end_date: Optional[datetime]
    status: BookingStatus
    checked_in_date: Optional[datetime]
    checked_in_source: CheckInOutSource
    check_in_method: Optional[CheckInOutMethod]

    check_out_source: CheckInOutSource
    check_out_method: Optional[CheckInOutMethod]
    checked_out_date: Optional[datetime]

    cancellation_reason: Optional[CancellationReason]
    cancelled_date: Optional[datetime]

    class Config:  # pylint: disable=missing-class-docstring
        use_enum_values = True
        validate_default = True
