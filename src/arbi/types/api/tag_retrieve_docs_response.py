# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .doc_tag_metadata import DocTagMetadata

__all__ = ["TagRetrieveDocsResponse", "Doc", "DocDocument"]


class DocDocument(BaseModel):
    external_id: str

    file_name: str

    status: str


class Doc(BaseModel):
    doc_tag_metadata: DocTagMetadata

    document: DocDocument


class TagRetrieveDocsResponse(BaseModel):
    docs: List[Doc]
