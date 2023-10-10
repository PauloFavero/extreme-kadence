from typing import List, Optional
from datetime import datetime

from pydantic import TypeAdapter

from domain.usecases import GetUserBookings
from domain.entities import AuthToken, Booking
from data.models import KadenceAuthToken, KadenceBooking
from data.protocols import GetUserBookingsHttp, KadenceGetBookingsQueryParams


class KadenceGetUserBookingsHttpPort(GetUserBookings):
    """Class representing the KadenceGetUserBookingsHttpPort"""

    def __init__(self, adapter: GetUserBookingsHttp) -> None:
        self._adapter = adapter

    def get(
        self,
        token: AuthToken,
        user_id: str,
        from_date: Optional[datetime] = None,
        page: Optional[int] = 1,
        itens_per_page: Optional[int] = 10,
    ) -> List[Booking]:
        """Get user by email"""
        kdc_token = KadenceAuthToken(
            access_token=token.token,
            token_type=token.type,
            expires_at=token.expire_at,
            expires_in=token.expire_in,
        )

        query_params = KadenceGetBookingsQueryParams(
            start_date=from_date, page=page, itens=itens_per_page
        )

        bookings: List[KadenceBooking] = self._adapter.get_bookings_by_user_id(
            token=kdc_token, user_id=user_id, query_params=query_params
        )

        return [Booking(**data.model_dump()) for data in bookings]
