"""Kadence Router Configuration"""

from http import HTTPStatus

from fastapi import APIRouter, Depends, HTTPException
from server.factories.kadence.fresh_token_factory import kadence_fresh_token_service_factory
from domain.entities import AuthToken
# from server.presentation.services.kadence.get_fresh_token import GetFreshKadenceTokenService
# from data.models import KadenceAuthToken
# from server.factories.kadence.auth_factory import kadence_auth_controller_factory
# from server.factories.kadence.get_user_bookings_factory import (
#     kadence_get_user_bookings_factory,
# )

from config.kadence import KadenceSettings

kadence_router = APIRouter(
    prefix="/kadence",
    tags=["Kadence Integration"],
)

kadence_settings = KadenceSettings()
# auth_controller = kadence_auth_controller_factory()
# bookings_controller = kadence_get_user_bookings_factory()

fresh_token_service = kadence_fresh_token_service_factory()

@kadence_router.get("/fresh-token", status_code=HTTPStatus.OK)
async def get_fresh_token() -> AuthToken:
    token = await fresh_token_service.handle()
    return token

# @kadence_router.get("/auth", status_code=HTTPStatus.OK)
# async def request_auth_token() -> KadenceAuthToken:
#     token = await auth_controller.handle()
#     return token


# @kadence_router.get(
#     "/user",
#     status_code=HTTPStatus.OK,
# )
# def get_user(token: KadenceAuthToken = Depends(auth_controller.handle)):
#     print(f"{datetime.now()} - GET /user")
#     user = requests.get(
#         f"{kadence_settings.base_uri}{kadence_settings.api_version}/users?email=phfaverop@gmail.com",
#         headers={"Authorization": f"{token.token_type} {token.access_token}"},
#     )
#     return user.json()


# @kadence_router.get(
#     "/user/bookings/{user_id}",
#     status_code=HTTPStatus.OK,
# )
# async def get_user_bookings(
#     user_id: str,
#     page: int = 1,
#     itens_per_page: int = 10,
#     token: KadenceAuthToken = Depends(auth_controller.handle),
# ) -> List[Booking]:
#     print(f"{datetime.now()} - GET /users/{user_id}/bookings")
#     if token is None or isinstance(token, KadenceAuthToken) is False:
#         raise HTTPException(
#             status_code=HTTPStatus.UNAUTHORIZED, detail=token.model_dump()
#         )

#     bookings = await bookings_controller.handle(
#         user_id=user_id, token=token, page=page, itens_per_page=itens_per_page
#     )
#     return bookings


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
