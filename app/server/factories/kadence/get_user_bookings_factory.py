from config import environment

from data.ports import KadenceGetUserBookingsHttpPort
from infra.adapters import GetUserBookingsHttpAdapter
from server.presentation.services.kadence.get_user_bookings import (
    GetKadenceUserBookingsService,
)


def get_kadence_user_bookings_factory() -> GetKadenceUserBookingsService:
    """Factory to get kadence user"""
    kdc_cfg = environment.kadence
    http_adapter = GetUserBookingsHttpAdapter(config=kdc_cfg)
    http_port = KadenceGetUserBookingsHttpPort(adapter=http_adapter)
    return GetKadenceUserBookingsService(port=http_port)
