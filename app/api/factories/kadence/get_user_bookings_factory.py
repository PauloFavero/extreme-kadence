from api.factories.kadence.auth_factory import kadence_auth_controller_factory
from domain.services.kadence.booking import KadenceGetUserBookingsService
from infra.http.kadence.bookings.get_user_bookings import GetUserBookingsRequester
from config.server import environment

kadence_config = environment.kadence

def kadence_get_user_bookings_factory() -> KadenceGetUserBookingsService:
    requester = GetUserBookingsRequester(kadence_config)
    return KadenceGetUserBookingsService(
        requester=requester,
        authenticator=kadence_auth_controller_factory(),
        config=kadence_config
    )