from datetime import datetime
from pydantic import BaseModel

from domain.entities.kadence.check_in import CheckInMethod
from domain.entities.kadence.space import Space


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

