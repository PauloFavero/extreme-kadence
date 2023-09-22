"""Kadence Router Configuration"""

from http import HTTPStatus
from datetime import datetime

import requests
from fastapi import APIRouter, Depends

from domain.models.kadence import KadenceAuthToken, AccessMethod
from usecases import kadence_auth


kadence_router = APIRouter(
    prefix="/kadence",
    tags=["Kadence Integration"],
)

BASE_URL = "https://api.onkadence.co/v1/public"


@kadence_router.get("/auth", status_code=HTTPStatus.OK)
def request_auth_token() -> KadenceAuthToken:
    token = kadence_auth()
    return token


@kadence_router.get(
    "/user",
    status_code=HTTPStatus.OK,
)
def get_user(token: KadenceAuthToken = Depends(kadence_auth)):
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
def get_user_bookings(user_id: str, token: KadenceAuthToken = Depends(kadence_auth)):
    print(f"{datetime.now()} - GET /users/{user_id}/bookings")
    bookings = requests.get(
        f"{BASE_URL}/users/{user_id}/bookings",
        headers={"Authorization": f"{token.token_type} {token.access_token}"},
    )
    return bookings.json()


@kadence_router.post(
    "/user/bookings/{booking_id}/checkin",
    status_code=HTTPStatus.OK,
)
def checkin_user(booking_id: str, user_id: str,
                 token: KadenceAuthToken = Depends(kadence_auth)):
    print(f"{datetime.now()} - POST /user/bookings/{booking_id}/checkin")
    checkin = requests.post(
        f"{BASE_URL}/bookings/{booking_id}/check-in",
        headers={"Authorization": f"{token.token_type} {token.access_token}"},
        json={"userId": user_id, "method": AccessMethod.WIFI.value},
    )
    return checkin.json()
