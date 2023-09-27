"""Kadence Router Configuration"""

from http import HTTPStatus
from datetime import datetime
from typing import List

import requests
from fastapi import APIRouter, Depends
from api.factories.kadence.auth_factory import kadence_auth_controller_factory
from domain.services.kadence.pagination import get_hydra_pagination
from domain.entities.kadence.booking import (
    Booking,
    BookingList,
    FetchBookingsFilterParams,
)

from config.kadence import KadenceSettings
from domain.entities.kadence import KadenceAuthToken, CheckInMethod

kadence_router = APIRouter(
    prefix="/kadence",
    tags=["Kadence Integration"],
)

auth_controller = kadence_auth_controller_factory()

kadence_settings = KadenceSettings()


@kadence_router.get("/auth", status_code=HTTPStatus.OK)
async def request_auth_token() -> KadenceAuthToken:
    token = await auth_controller.handle()
    return token


@kadence_router.get(
    "/user",
    status_code=HTTPStatus.OK,
)
def get_user(token: KadenceAuthToken = Depends(auth_controller.handle)):
    print(f"{datetime.now()} - GET /user")
    user = requests.get(
        f"{kadence_settings.base_uri}{kadence_settings.api_version}/users?email=phfaverop@gmail.com",
        headers={"Authorization": f"{token.token_type} {token.access_token}"},
    )
    return user.json()


@kadence_router.get(
    "/user/bookings/{user_id}",
    status_code=HTTPStatus.OK,
)
def get_user_bookings(
    user_id: str, token: KadenceAuthToken = Depends(auth_controller.handle)
) -> List[Booking]:
    print(f"{datetime.now()} - GET /users/{user_id}/bookings")
    query_params = FetchBookingsFilterParams()
    response = requests.get(
        f"{kadence_settings.base_uri}{kadence_settings.api_version}/users/{user_id}/bookings",
        headers={"Authorization": f"{token.token_type} {token.access_token}"},
        params=query_params.model_dump(by_alias=True),
    )
    bookings = response.json()
    pagination = get_hydra_pagination(bookings)
    bookings_list = BookingList(itens=bookings.get("hydra:member", []))

    ## fetch corresponding bookings
    while pagination and pagination.next:
        response = requests.get(
            f"{kadence_settings.base_uri}{pagination.next}",
            headers={"Authorization": f"{token.token_type} {token.access_token}"},
            # params=query_params.model_dump(by_alias=True),
        )
        bookings = response.json()
        pagination = get_hydra_pagination(bookings)
        bookings_list.itens.extend(bookings.get("hydra:member", []))

    return bookings_list.itens


@kadence_router.post(
    "/user/bookings/{booking_id}/checkin",
    status_code=HTTPStatus.OK,
)
def checkin_user(
    booking_id: str,
    user_id: str,
    token: KadenceAuthToken = Depends(auth_controller.handle),
):
    print(f"{datetime.now()} - POST /user/bookings/{booking_id}/checkin")
    checkin = requests.post(
        f"{kadence_settings.base_uri}{kadence_settings.api_version}/bookings/{booking_id}/check-in",
        headers={"Authorization": f"{token.token_type} {token.access_token}"},
        json={"userId": user_id, "method": CheckInMethod.WIFI.value},
    )
    return checkin.json()
