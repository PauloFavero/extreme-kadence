from pydantic import BaseModel
from http import HTTPMethod, HTTPStatus
from typing import Optional, TypeVar, Generic, Any

T = TypeVar('T')

class HttpRequestConfig(BaseModel, Generic[T]):
    url: str
    method: HTTPMethod
    headers: dict
    data: Optional[T] = None


class HttpResponse(BaseModel, Generic[T]):
    status_code: HTTPStatus
    body: T