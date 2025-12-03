# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from datetime import date
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["DocumentUpdateParams", "Document"]


class DocumentUpdateParams(TypedDict, total=False):
    documents: Required[Iterable[Document]]

    workspace_key: Annotated[str, PropertyInfo(alias="workspace-key")]


class Document(TypedDict, total=False):
    external_id: Required[str]

    doc_date: Annotated[Union[str, date, None], PropertyInfo(format="iso8601")]

    shared: Optional[bool]

    title: Optional[str]
