# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .doc_tag_metadata import DocTagMetadata

__all__ = ["DocumentRetrieveTagsResponse", "Tag", "TagTag"]


class TagTag(BaseModel):
    external_id: str

    name: str


class Tag(BaseModel):
    doc_tag_metadata: DocTagMetadata

    tag: TagTag


class DocumentRetrieveTagsResponse(BaseModel):
    tags: List[Tag]
