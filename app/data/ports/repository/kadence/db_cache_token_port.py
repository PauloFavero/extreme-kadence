from domain.entities import AuthToken
from domain.usecases import CacheToken
from data.protocols import CacheTokenRepo


class DbCacheTokenPort(CacheToken):
    """Cache db port implementation"""

    def __init__(self, token_repository: CacheTokenRepo):
        self.token_repository = token_repository

    def cache(self, token: AuthToken) -> None:
        """Method to cache token"""

        self.token_repository.persist(token)
