from datetime import datetime
from typing import List, Optional

from domain.entities import AuthToken, Booking
from domain.usecases import GetUserBookings


class GetKadenceUserBookingsService:
    def __init__(
        self,
        port: GetUserBookings,
    ) -> None:
        self.port = port

    def handle(
        self,
        token: AuthToken,
        user_id: str,
        from_date: Optional[datetime] = None,
        page: Optional[int] = 1,
        itens_per_page: Optional[int] = 10,
    ) -> List[Booking]:
        bookings: List[Booking] = self.port.get(
            token=token,
            user_id=user_id,
            from_date=from_date,
        )

        return bookings
