# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["ConfigUpdateResponse"]


class ConfigUpdateResponse(BaseModel):
    created_at: str

    external_id: str

    title: Optional[str] = None
