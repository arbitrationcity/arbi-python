# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["DocTagMetadata"]


class DocTagMetadata(BaseModel):
    created_at: datetime

    external_id: str

    updated_at: datetime

    note: Optional[str] = None

    page_ref: Optional[int] = None
