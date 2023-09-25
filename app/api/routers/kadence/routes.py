"""Kadence Router Configuration"""

from http import HTTPStatus
from datetime import datetime
from typing import List

import requests
from fastapi import APIRouter, Depends
from api.factories.kadence.auth_factory import kadence_auth_controller_factory
from domain.entities.kadence.booking import Booking

from domain.entities.kadence import KadenceAuthToken, CheckInMethod

kadence_router = APIRouter(
    prefix="/kadence",
    tags=["Kadence Integration"],
)

BASE_URL = "https://api.onkadence.co/v1/public"

auth_controller = kadence_auth_controller_factory()


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
        f"{BASE_URL}/users?email=phfaverop@gmail.com",
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
    bookings = requests.get(
        f"{BASE_URL}/users/{user_id}/bookings",
        headers={"Authorization": f"{token.token_type} {token.access_token}"},
    )

    return bookings.json().get("hydra:member", [])


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
        f"{BASE_URL}/bookings/{booking_id}/check-in",
        headers={"Authorization": f"{token.token_type} {token.access_token}"},
        json={"userId": user_id, "method": CheckInMethod.WIFI.value},
    )
    return checkin.json()
