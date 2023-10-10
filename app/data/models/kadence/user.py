from datetime import datetime
from typing import Optional
from enum import Enum

from pydantic import BaseModel, EmailStr, Field


class TimePreference(str, Enum):
    """Time Preference Enum"""

    DEFAULT = "default"
    AM_PM = "12H"
    FULL = "24H"


class KadenceUser(BaseModel):
    """Kadence User model"""

    id: str = Field(alias="id")
    type: str = Field(alias="@type")
    email: EmailStr = Field(alias="email")
    first_name: str = Field(alias="firstName")
    last_name: str = Field(alias="lastName")
    job_title: Optional[str] = Field(alias="jobTitle")
    invitation_pending: bool = Field(alias="invitationPending")
    created_at: datetime = Field(alias="createdAt")
    modified_at: datetime = Field(alias="modifiedAt")
    locale: str = Field(alias="locale")
    time_preference: TimePreference = Field(alias="timePreference")
    location_city_name: Optional[str] = Field(alias="locationCityName")
    location_country_code: Optional[str] = Field(alias="locationCountryCode")
    location_latitude: Optional[float] = Field(alias="locationLatitude")
    location_longitude: Optional[float] = Field(alias="locationLongitude")
    monogram: str = Field(alias="monogram")

    class Config:  # pylint: disable=missing-class-docstring
        use_enum_values = True
        validate_default = True
