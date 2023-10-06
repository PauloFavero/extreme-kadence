from typing import Optional

from domain.usecases import GetUser
from domain.entities import AuthToken, User


class GetKadenceUserService:
    def __init__(
        self,
        kadence_port: GetUser,
    ) -> None:
        self.kadence_port = kadence_port

    async def handle(self, token: AuthToken, user_email: str) -> Optional[User]:
        try:
            user = await self.kadence_port.get_user(token=token, user_email=user_email)
            return user
        except Exception as error:
            print("Error while fetching Kadence user: ", error)
            return error
