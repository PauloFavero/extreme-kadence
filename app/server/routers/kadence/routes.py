"""Kadence Router Configuration"""
from datetime import datetime
from http import HTTPStatus
from typing import List, Optional

from fastapi import APIRouter, Depends, HTTPException
from server.factories.kadence.get_user_bookings_factory import (
    get_kadence_user_bookings_factory,
)
from server.factories.kadence.get_user_factory import get_kadence_user_factory
from server.factories.kadence.fresh_token_factory import (
    kadence_fresh_token_service_factory,
)
from domain.entities import AuthToken, User, Booking

from server.factories.kadence.auth_factory import kadence_auth_controller_factory

from config.kadence import KadenceSettings

kadence_router = APIRouter(
    prefix="/kadence",
    tags=["Kadence Integration"],
)

kadence_settings = KadenceSettings()

fresh_token_service = kadence_fresh_token_service_factory()
auth_controller = kadence_auth_controller_factory()
get_user_service = get_kadence_user_factory()
bookings_controller = get_kadence_user_bookings_factory()


@kadence_router.get("/fresh-token", status_code=HTTPStatus.OK)
async def get_fresh_token() -> AuthToken:
    """Get fresh token from Kadence API"""
    token = await fresh_token_service.handle()
    return token


@kadence_router.get("/auth", status_code=HTTPStatus.OK)
async def request_auth_token() -> AuthToken:
    """Get kadence authentication token"""
    token = await auth_controller.handle()
    return token


@kadence_router.get(
    "/user",
    status_code=HTTPStatus.OK,
)
async def get_user(
    user_email: str, token: AuthToken = Depends(auth_controller.handle)
) -> User:
    user = await get_user_service.handle(token=token, user_email=user_email)
    return user


@kadence_router.get(
    "/user/bookings/{user_id}",
    status_code=HTTPStatus.OK,
)
async def get_user_bookings(
    user_id: str,
    from_date: Optional[datetime] = None,
    page: Optional[int] = 1,
    itens_per_page: Optional[int] = 10,
    token: AuthToken = Depends(auth_controller.handle),
) -> List[Booking]:
    print(f"{datetime.now()} - GET /users/{user_id}/bookings")
    if token is None:
        raise HTTPException(status_code=HTTPStatus.UNAUTHORIZED)

    bookings: List[Booking] = bookings_controller.handle(
        token=token,
        user_id=user_id,
        from_date=from_date,
        page=page,
        itens_per_page=itens_per_page,
    )
    return bookings


# @kadence_router.post(
#     "/user/bookings/{booking_id}/checkin",
#     status_code=HTTPStatus.OK,
# )
# def checkin_user(
#     booking_id: str,
#     user_id: str,
#     token: KadenceAuthToken = Depends(auth_controller.handle),
# ):
#     print(f"{datetime.now()} - POST /user/bookings/{booking_id}/checkin")
#     checkin = requests.post(
#         f"{kadence_settings.base_uri}{kadence_settings.api_version}/bookings/{booking_id}/check-in",
#         headers={"Authorization": f"{token.token_type} {token.access_token}"},
#         json={"userId": user_id, "method": CheckInMethod.WIFI.value},
#     )
#     return checkin.json()
