from typing import Optional
from pydantic import BaseModel, Field


class HydraPagination(BaseModel):
    """Hydra pagination model. ( "hydra:view") """
    id: str = Field(alias="@id")
    type: str = Field(alias="@type")
    first: Optional[str] = Field(alias="hydra:first", default=None)
    last: Optional[str] = Field(alias="hydra:last", default=None)
    next: Optional[str] = Field(alias="hydra:next", default=None)
    previous: Optional[str] = Field(alias="hydra:previous", default=None)

    