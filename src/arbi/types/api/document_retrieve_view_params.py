# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["DocumentRetrieveViewParams"]


class DocumentRetrieveViewParams(TypedDict, total=False):
    page: Optional[int]
    """Optional page to open on load"""
