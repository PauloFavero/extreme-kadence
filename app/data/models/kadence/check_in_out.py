from enum import Enum


class CheckInMethod(Enum):
    DOOR = "door"
    WIFI = "wifi"
    GEOFENCE = "front_desk"
    SENSOR = "sensor"
    UNKNOWN = "unknown"


class CheckInSource(Enum):
    WEB = "web"
    IOS = "ios"
    ANDROID = "android"
    CALENDAR = "calendar"
    PUBLICAPI = "publicApi"
    SLACK = "slack"
    MSTEAMS = "msTeams"
    UNKNOWN = "unknown"
