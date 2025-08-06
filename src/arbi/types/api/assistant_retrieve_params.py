# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = [
    "AssistantRetrieveParams",
    "Tools",
    "ToolsModelCitationTool",
    "ToolsRetrievalChunkToolInput",
    "ToolsRetrievalChunkToolInputToolResponse",
    "ToolsRetrievalChunkToolInputToolResponseMetadata",
    "ToolsRetrievalFullContextToolInput",
    "ToolsRetrievalFullContextToolInputToolResponse",
    "ToolsRetrievalFullContextToolInputToolResponseMetadata",
]


class AssistantRetrieveParams(TypedDict, total=False):
    content: Required[str]

    workspace_ext_id: Required[str]

    parent_message_ext_id: Optional[str]

    tools: Dict[str, Tools]


class ToolsModelCitationTool(TypedDict, total=False):
    description: str

    name: Literal["model_citation"]

    tool_responses: Dict[str, List[str]]


class ToolsRetrievalChunkToolInputToolResponseMetadata(TypedDict, total=False):
    chunk_doc_idx: Required[int]

    chunk_ext_id: Required[str]

    chunk_pg_idx: Required[int]

    created_at: Required[str]

    page_number: Required[int]

    chunk_id: Optional[str]

    doc_ext_id: Optional[str]

    doc_title: Optional[str]

    rerank_score: Optional[float]

    score: Optional[float]

    tokens: Optional[int]


class ToolsRetrievalChunkToolInputToolResponse(TypedDict, total=False):
    content: Required[str]

    metadata: Required[ToolsRetrievalChunkToolInputToolResponseMetadata]


class ToolsRetrievalChunkToolInput(TypedDict, total=False):
    description: str

    name: Literal["retrieval_chunk"]

    tool_args: Dict[str, List[str]]

    tool_responses: Dict[str, Iterable[ToolsRetrievalChunkToolInputToolResponse]]


class ToolsRetrievalFullContextToolInputToolResponseMetadata(TypedDict, total=False):
    chunk_doc_idx: Required[int]

    chunk_ext_id: Required[str]

    chunk_pg_idx: Required[int]

    created_at: Required[str]

    page_number: Required[int]

    chunk_id: Optional[str]

    doc_ext_id: Optional[str]

    doc_title: Optional[str]

    rerank_score: Optional[float]

    score: Optional[float]

    tokens: Optional[int]


class ToolsRetrievalFullContextToolInputToolResponse(TypedDict, total=False):
    content: Required[str]

    metadata: Required[ToolsRetrievalFullContextToolInputToolResponseMetadata]


class ToolsRetrievalFullContextToolInput(TypedDict, total=False):
    description: str

    name: Literal["retrieval_full_context"]

    tool_args: Dict[str, List[str]]

    tool_responses: Dict[str, Iterable[ToolsRetrievalFullContextToolInputToolResponse]]


Tools: TypeAlias = Union[ToolsModelCitationTool, ToolsRetrievalChunkToolInput, ToolsRetrievalFullContextToolInput]
