from typing import Any, Dict, Optional, Tuple, List
from pydantic import TypeAdapter

import requests
from requests import Response

from config.kadence import KadenceSettings
from data.protocols import GetUserBookingsHttp, KadenceGetBookingsQueryParams
from data.models import (
    KadenceAuthToken,
    HydraPagination,
    KadenceBooking,
)
from server.presentation.services.kadence.pagination import get_hydra_pagination


class GetUserBookingsHttpAdapter(GetUserBookingsHttp):
    """Get User Bookings Adapter"""

    def __init__(self, config: KadenceSettings) -> None:
        super().__init__()
        self.__session = requests.Session()
        self.__config = config

    def __handle_bookings_response(
        self, response: Response
    ) -> Tuple[List[KadenceBooking], Optional[HydraPagination]]:
        bookings: Dict[str, Any] = response.json()
        pagination = get_hydra_pagination(bookings)
        bookings_list = TypeAdapter(List[KadenceBooking]).validate_python(
            bookings.get("hydra:member", [])
        )

        return bookings_list, pagination

    def __get_bookings_from_pagination(
        self,
        token: KadenceAuthToken,
        pagination: HydraPagination,
    ) -> Tuple[List[KadenceBooking], Optional[HydraPagination]]:
        response = self.__session.get(
            url=pagination.next,
            headers={"Authorization": f"{token.token_type} {token.access_token}"},
        )
        return self.__handle_bookings_response(response)

    def get_bookings_by_user_id(
        self,
        token: KadenceAuthToken,
        user_id: str,
        query_params: Optional[KadenceGetBookingsQueryParams] = None,
    ) -> List[KadenceBooking]:
        response = self.__session.get(
            url=f"{self.__config.base_uri}{self.__config.api_version}/users/{user_id}/bookings",
            headers={"Authorization": f"{token.token_type} {token.access_token}"},
            params=query_params.model_dump(by_alias=True, exclude_none=True)
            if query_params
            else None,
        )

        bookings_list, pagination = self.__handle_bookings_response(response)
        while pagination and pagination.next:
            (
                bookings_next_page,
                pagination,
            ) = self.__get_bookings_from_pagination(token=token, pagination=pagination)
            bookings_list.extend(bookings_next_page)
        return bookings_list
