from typing import Optional, Tuple
import requests
from app.data.protocols.kadence.booking.get_user_bookings_http import (
    GetUserBookingsHttpProtocol,
)
from server.presentation.services.kadence.pagination import get_hydra_pagination
from data.models import (
    KadenceAuthToken,
    HydraPagination,
    BookingList,
    FetchBookingsFilterParams,
)
from config.kadence import KadenceSettings


class GetUserBookingsRequester(GetUserBookingsHttpProtocol):
    def __init__(self, config: KadenceSettings) -> None:
        super().__init__()
        self.__session = requests.Session()
        self.__config = config

    def get_bookings_by_user_id(
        self,
        user_id: str,
        token: KadenceAuthToken,
        filter: Optional[FetchBookingsFilterParams] = None,
    ) -> Tuple[BookingList, Optional[HydraPagination]]:
        response = self.__session.get(
            url=f"{self.__config.base_uri}{self.__config.api_version}/users/{user_id}/bookings",
            headers={"Authorization": f"{token.token_type} {token.access_token}"},
            params=filter.model_dump(by_alias=True) if filter else None,
        )
        bookings = response.json()
        pagination = get_hydra_pagination(bookings)
        bookings_list = BookingList(itens=bookings.get("hydra:member", []))
        return bookings_list, pagination

    def get_bookings_from_pagination(
        self,
        pagination: HydraPagination,
        token: KadenceAuthToken,
    ) -> Tuple[BookingList, Optional[HydraPagination]]:
        response = self.__session.get(
            url=pagination.next,
            headers={"Authorization": f"{token.token_type} {token.access_token}"},
        )
        bookings = response.json()
        pagination = get_hydra_pagination(bookings)
        bookings_list = BookingList(itens=bookings.get("hydra:member", []))
        return bookings_list, pagination
