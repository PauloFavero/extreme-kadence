from data.models import KadenceAuthToken
from infra.databases.redis import RedisSingleton


class KadenceAuthRepo:
    def __init__(self, db: RedisSingleton) -> None:
        super().__init__()
        self.__db = db

    async def persist(self, token: KadenceAuthToken) -> None:
        print("redis persist token", token)
        self.__db.set("kadence_token", token.access_token, ex=token.expires_in, nx=True)
        self.__db.set(
            "kadence_token_type", token.token_type, ex=token.expires_in, nx=True
        )
        self.__db.set(
            "kadence_token_expires_at", token.expires_at, ex=token.expires_in, nx=True
        )
        self.__db.set(
            "kadence_token_expires_in", token.expires_in, ex=token.expires_in, nx=True
        )

    async def delete(self) -> None:
        self.__db.delete("kadence_token")
        self.__db.delete("kadence_token_type")
        self.__db.delete("kadence_token_expires_at")
        self.__db.delete("kadence_token_expires_in")

    async def get_cached_token(self) -> KadenceAuthToken:
        access_token, token_type, exp_in, exp_at = self.__db.getmany(
            [
                "kadence_token",
                "kadence_token_type",
                "kadence_token_expires_in",
                "kadence_token_expires_at",
            ]
        )
        if access_token and token_type:
            return KadenceAuthToken(
                access_token=access_token,
                token_type=token_type,
                expires_in=exp_in,
                expires_at=exp_at,
            )

        return None
