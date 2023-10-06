from typing import Optional

from pydantic import BaseModel

from domain.entities import SpaceType, Floor, Neighborhood


class KadenceSpace(BaseModel):
    """Space Model"""

    id: str
    name: str
    type: SpaceType
    floor: Optional[Floor]
    neighborhood: Optional[Neighborhood]
