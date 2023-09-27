from typing import Dict, Optional

from domain.entities.kadence.pagination import HydraPagination

def get_hydra_pagination(pagination_data: Dict[str, str]) -> Optional[HydraPagination]:
    """Get hydra pagination data from a dict."""
    hidra_view = pagination_data.get("hydra:view", None)
    return HydraPagination(**hidra_view) if hidra_view else None