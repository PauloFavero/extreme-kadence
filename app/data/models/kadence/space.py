from typing import Optional
from pydantic import BaseModel


class Neighborhood(BaseModel):
    """Neighborhood Model"""

    id: str
    name: str


class Floor(BaseModel):
    """Floor Model"""

    id: str
    name: str


class Space(BaseModel):
    """Space Model"""

    id: str
    name: str
    type: str
    floor: Optional[Floor]
    neighborhood: Optional[Neighborhood]
