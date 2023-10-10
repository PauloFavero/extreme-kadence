from typing import Optional


from data.protocols import CacheTokenRepo, GetCachedTokenRepo
from data.models import KadenceAuthToken
from infra.databases.redisCache import RedisSingleton


class DdKadenceTokenCacheRepository(GetCachedTokenRepo, CacheTokenRepo):
    """Kadence Authentication Repository"""

    def __init__(self) -> None:
        super().__init__()
        self.__db = RedisSingleton()

    def get(self) -> Optional[KadenceAuthToken]:
        """Get cached token from redis"""
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

    def persist(self, token: KadenceAuthToken) -> None:
        """Persist token in redis"""
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
