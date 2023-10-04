from http import HTTPMethod, HTTPStatus
from typing import Optional, TypeVar, Generic, Dict

from pydantic import BaseModel

T = TypeVar("T")


class HttpRequestConfig(BaseModel, Generic[T]):
    """Http Request Config Model"""

    url: str
    method: HTTPMethod
    headers: Dict[str, str | int | float | bool]
    data: Optional[T] = None


class HttpResponse(BaseModel, Generic[T]):
    """Http Response Model"""

    status_code: HTTPStatus
    body: T
