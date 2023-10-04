from infra.adapters.http.kadence.get_user_bookings import GetUserBookingsRequester
from server.presentation.services.kadence.booking import KadenceGetUserBookingsService
from config.server import environment

kadence_config = environment.kadence


def kadence_get_user_bookings_factory() -> KadenceGetUserBookingsService:
    """Factory to get user bookings from Kadence API"""
    requester = GetUserBookingsRequester(kadence_config)
    return KadenceGetUserBookingsService(requester=requester, config=kadence_config)
