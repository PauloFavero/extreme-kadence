from typing import Optional
from pydantic import BaseModel, Field


class HydraPagination(BaseModel):
    """Hydra pagination model. ( "hydra:view") """
    id: str = Field(alias="@id")
    type: str = Field(alias="@type")
    first: Optional[str] = Field(alias="hydra:first")
    last: Optional[str] = Field(alias="hydra:last")
    next: Optional[str] = Field(alias="hydra:next")
    previous: Optional[str] = Field(alias="hydra:previous")

    