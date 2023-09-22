import time

from api import server
from http import HTTPStatus
from fastapi import Request, HTTPException

from usecases.kadence.req_auth_token import get_auth_token
from domain.models.kadence.authentication import KadenceAuthToken


@server.middleware("http")
async def kadence_auth(request: Request, call_next):
    try:
        token: KadenceAuthToken = get_auth_token()
        request.headers["Authorization"] = f"{token.token_type} {token.access_token}"
        response = await call_next(request)
        return response
    except Exception as error:
        print("Kadence auth middleware error: ", error)
        raise HTTPException(status_code=HTTPStatus.UNAUTHORIZED, detail=error.__str__())
