from data.models import KadenceAuthToken
from data.protocols import GetCachedTokenRepo, CacheTokenRepo
from domain.usecases import GetCachedToken, CacheToken
from domain.entities import AuthToken


class DbKadenceTokenCachePort(GetCachedToken, CacheToken):
    """Cache db port implementation"""

    def __init__(
        self, set_cache_adapter: CacheTokenRepo, get_cache_adapter: GetCachedTokenRepo
    ):
        self.get_cache_adapter = get_cache_adapter
        self.set_cache_adapter = set_cache_adapter

    def get(self) -> AuthToken:
        """Method to get a cached token"""

        token = self.get_cache_adapter.get()
        if token:
            return AuthToken(
                token=token.access_token,
                type=token.token_type,
                expire_at=token.expires_at,
                expire_in=token.expires_in,
            )
        return None

    def cache(self, token: AuthToken) -> None:
        """Method to cache token"""

        token = KadenceAuthToken(
            access_token=token.token,
            token_type=token.type,
            expires_at=token.expire_at,
            expires_in=token.expire_in,
        )

        self.set_cache_adapter.persist(token)
