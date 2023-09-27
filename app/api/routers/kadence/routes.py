"""Kadence Router Configuration"""

from http import HTTPStatus
from datetime import datetime
from typing import List

import requests
from fastapi import APIRouter, Depends
from api.factories.kadence.auth_factory import kadence_auth_controller_factory
from api.factories.kadence.get_user_bookings_factory import (
    kadence_get_user_bookings_factory,
)
from domain.entities.kadence.booking import (
    Booking,
)

from config.kadence import KadenceSettings
from domain.entities.kadence import KadenceAuthToken, CheckInMethod

kadence_router = APIRouter(
    prefix="/kadence",
    tags=["Kadence Integration"],
)

kadence_settings = KadenceSettings()
auth_controller = kadence_auth_controller_factory()
bookings_controller = kadence_get_user_bookings_factory()


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
async def get_user_bookings(
    user_id: str, page: int = 1, itens_per_page: int = 10
) -> List[Booking]:
    print(f"{datetime.now()} - GET /users/{user_id}/bookings")
    bookings = await bookings_controller.handle(
        user_id=user_id, page=page, itens_per_page=itens_per_page
    )
    return bookings


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
