# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, TypedDict

from ..._types import FileTypes

__all__ = ["DocumentUploadParams"]


class DocumentUploadParams(TypedDict, total=False):
    workspace_ext_id: Required[str]

    files: Required[List[FileTypes]]
    """Multiple files to upload"""

    shared: bool
    """Whether the document should be shared with workspace members"""
