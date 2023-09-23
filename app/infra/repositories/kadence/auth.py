
import time
from domain.entities.kadence.auth import KadenceAuthToken
from domain.protocols.kadence.auth_repo import AuthenticationRepoProtocol
from infra.databases.redis import RedisSingleton


class KadenceAuthRepo(AuthenticationRepoProtocol):

    def __init__(self, db: RedisSingleton) -> None:
        super().__init__()
        self.__db = db
    
    async def persist(self, token: KadenceAuthToken) -> None:
        self.__db.set("kadence_token", token.access_token)
        self.__db.set("kadence_token_type", token.token_type)
        self.__db.set("kadence_token_expires_in", token.expires_in + int(time()) - 60)

    async def delete(self) -> None:
        self.__db.delete("kadence_token")
        self.__db.delete("kadence_token_type")
        self.__db.delete("kadence_token_expires_in")

    async def get_cached_token(self) -> KadenceAuthToken:
        access_token = self.__db.get("kadence_token")
        token_type = self.__db.get("kadence_token_type")
        expires_in = self.__db.get("kadence_token_expires_in")
        if access_token and token_type and expires_in:
            return KadenceAuthToken(
                access_token=str(access_token),
                token_type=str(token_type),
                expires_in=int(expires_in.decode("utf-8")),
            )

        return None