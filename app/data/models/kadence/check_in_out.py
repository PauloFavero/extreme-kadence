from enum import Enum


class CheckInMethod(Enum):
    """Check in method."""

    DOOR = "door"
    WIFI = "wifi"
    GEOFENCE = "front_desk"
    SENSOR = "sensor"
    UNKNOWN = "unknown"


class CheckInSource(Enum):
    """Check in source."""

    WEB = "web"
    IOS = "ios"
    ANDROID = "android"
    CALENDAR = "calendar"
    PUBLICAPI = "publicApi"
    SLACK = "slack"
    MSTEAMS = "msTeams"
    UNKNOWN = "unknown"
