from infra.adapters.http.kadence.fresh_token_adapter import (
    KadenceFreshTokenHttpAdapter,
)
from data.ports import KadenceFreshTokenHttpPort
from server.presentation.services.kadence.get_fresh_token import (
    GetFreshKadenceTokenService,
)
from server.presentation.auth_middleware import AuthMiddleware
from config.server import environment

kadence_config = environment.kadence

def kadence_fresh_token_service_factory() -> AuthMiddleware:
    adapter = KadenceFreshTokenHttpAdapter(kadence_config)
    port = KadenceFreshTokenHttpPort(http_adapter=adapter)
    return GetFreshKadenceTokenService(
        kadence_port=port,
    )
