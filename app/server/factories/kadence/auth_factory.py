from data.ports import KadenceFreshTokenHttpPort, DbKadenceTokenCachePort
from infra.adapters import KadenceFreshTokenHttpAdapter, DdKadenceTokenCacheRepository

from server.presentation.services.kadence.auth import KadenceAuthService
from server.presentation.auth_middleware import AuthMiddleware
from config import environment


def kadence_auth_controller_factory() -> AuthMiddleware:
    """Kadence auth controller factory"""
    db_cache_adapter = DdKadenceTokenCacheRepository()
    db_cache_port = DbKadenceTokenCachePort(db_cache_adapter, db_cache_adapter)

    http_adapter = KadenceFreshTokenHttpAdapter(environment.kadence)
    http_port = KadenceFreshTokenHttpPort(http_adapter)

    return KadenceAuthService(cache_port=db_cache_port, http_port=http_port)
