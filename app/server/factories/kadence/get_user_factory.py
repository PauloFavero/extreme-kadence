from data.ports import KadenceGetUserHttpPort
from infra.adapters import KadenceGetUserHttpAdapter
from server.presentation.services.kadence.get_user import GetKadenceUserService
from config import environment


def get_kadence_user_factory() -> GetKadenceUserService:
    """Factory to get kadence user"""
    kdc_cfg = environment.kadence
    http_adapter = KadenceGetUserHttpAdapter(config=kdc_cfg)
    http_port = KadenceGetUserHttpPort(adapter=http_adapter)
    return GetKadenceUserService(kadence_port=http_port)
