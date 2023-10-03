from typing import Optional
from pydantic import BaseModel


class Neighborhood(BaseModel):
    id: str
    name: str


class Floor(BaseModel):
    id: str
    name: str


class Space(BaseModel):
    id: str
    name: str
    type: str
    floor: Optional[Floor]
    neighborhood: Optional[Neighborhood]
