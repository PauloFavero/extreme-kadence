from domain.protocols.auth_middleware import AuthMiddleware
from config.kadence import KadenceSettings
from domain.protocols.kadence import GetUserBookingsHttpProtocol
from domain.entities.kadence import (
    BookingList,
    FetchBookingsFilterParams,
    KadenceAuthToken,
)


class KadenceGetUserBookingsService:
    def __init__(
        self,
        requester: GetUserBookingsHttpProtocol,
        config: KadenceSettings,
    ) -> None:
        self.requester = requester
        self.config = config

    async def handle(
        self, user_id: str, token: KadenceAuthToken, page=1, itens_per_page: int = 10
    ) -> BookingList:
        if token is None or isinstance(token, KadenceAuthToken) is False:
            raise Exception("Invalid token")

        filter = FetchBookingsFilterParams(
            page=page, itens_per_page=itens_per_page
        )
        bookings, pagination = self.requester.get_bookings_by_user_id(
            user_id=user_id, token=token, filter=filter
        )

        while pagination and pagination.next:
            (
                bookings_next_page,
                pagination,
            ) = self.requester.get_bookings_from_pagination(
                pagination=pagination, token=token
            )
            bookings.itens.extend(bookings_next_page.itens)

        return bookings.itens
