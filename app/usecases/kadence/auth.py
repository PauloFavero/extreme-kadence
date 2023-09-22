from typing import Union, Tuple
import requests
from http import HTTPStatus
from time import time

from domain.models.kadence.authentication import (
    KadenceAuthTokenBodyReq,
    KadenceAuthToken,
    KadenceAuthError,
)
from infra.redis import RedisSingleton as Redis
from config import environment

kadence_config = environment.kadence

def get_cached_token_data() -> Union[KadenceAuthToken, None]:
    redis = Redis()
    token = redis.get("kadence_token")
    token_type = redis.get("kadence_token_type")
    expires_in = redis.get("kadence_token_expires_in")

    if token and token_type and expires_in:
        return KadenceAuthToken(
            access_token=str(token),
            token_type=str(token_type),
            expires_in=int(expires_in.decode("utf-8")),
        )

    return None


def validate_expiration_token(token: KadenceAuthToken) -> bool:
    curr_time = int(time())
    expires_in = int(token.expires_in)
    if curr_time < expires_in - 60:
        return True

    return False


def request_auth_token() -> Tuple[HTTPStatus, KadenceAuthToken]:
    body_req = KadenceAuthTokenBodyReq(client_id=kadence_config.identifier, 
                                       client_secret=kadence_config.secret)
    response = requests.post(url=kadence_config.login_endpoint,
                             data=body_req.model_dump())

    if response.status_code == HTTPStatus.OK:
        return HTTPStatus.OK, KadenceAuthToken(**response.json())

    raise Exception(KadenceAuthError(**response.json()))


def kadence_auth() -> KadenceAuthToken:
    cached_token = get_cached_token_data()

    if cached_token and validate_expiration_token(cached_token):
        print("Using cached token", cached_token)
        return cached_token

    else:
        redis = Redis()
        try:
            _, token = request_auth_token()

            redis.set("kadence_token", token.access_token)
            redis.set("kadence_token_type", token.token_type)
            redis.set("kadence_token_expires_in", token.expires_in)
            return token

        except Exception as error:
            print(
                "Error while fetching Kadence token: ",
                error,
            )
            redis.delete("kadence_token")
            redis.delete("kadence_token_type")
            redis.delete("kadence_token_expires_in")

            raise error
