from domain.entities import AuthToken

from domain.usecases import GetFreshToken
from server.presentation.auth_middleware import AuthMiddleware



class GetFreshKadenceTokenService(AuthMiddleware):
    def __init__(
        self,
        kadence_port: GetFreshToken,
    ) -> None:
        self.kadence_port = kadence_port

    async def handle(self) -> AuthToken:
        try:
            token = await self.kadence_port.get()
            return token
        except Exception as error:
            print("Error while fetching Kadence token: ", error)
            return error
