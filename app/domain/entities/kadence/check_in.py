from enum import Enum


class CheckInMethod(Enum):
    DOOR = "door"
    WIFI = "wifi"
    GEOFENCE = "front_desk"
    SENSOR = "sensor"
