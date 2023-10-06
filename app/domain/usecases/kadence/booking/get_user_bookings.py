from datetime import datetime
from abc import ABC, abstractmethod
from typing import List, Optional

from domain.entities import AuthToken, Booking


class GetUserBookings(ABC):
    """Class representing the GetUserBookings"""

    @abstractmethod
    def get(
        self, token: AuthToken, user_id: str, from_date: Optional[datetime] = None
    ) -> List[Booking]:
        """Get user Bookings from a given date"""
        raise NotImplementedError()
