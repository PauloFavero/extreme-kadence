from domain.protocols.controller import Controller
from domain.services.kadence.auth import KadenceAuthService
from infra.databases.redis import RedisSingleton
from infra.http.kadence.auth import KadenceAuthRequester
from infra.repositories.kadence.auth import KadenceAuthRepo
from config.server import environment

kadence_config = environment.kadence

def kadence_auth_controller_factory() -> Controller:
    db = RedisSingleton()
    repository = KadenceAuthRepo(db)
    requester = KadenceAuthRequester(kadence_config)
    return KadenceAuthService(
        repo=repository,
        requester=requester,
        config=kadence_config
    )