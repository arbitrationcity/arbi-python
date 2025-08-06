# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypeAlias

from ..._utils import PropertyInfo
from ..._models import BaseModel

__all__ = [
    "ConversationRetrieveThreadsResponse",
    "Thread",
    "ThreadHistory",
    "ThreadHistoryTools",
    "ThreadHistoryToolsModelCitationTool",
    "ThreadHistoryToolsRetrievalChunkToolOutput",
    "ThreadHistoryToolsRetrievalChunkToolOutputToolResponse",
    "ThreadHistoryToolsRetrievalChunkToolOutputToolResponseMetadata",
    "ThreadHistoryToolsRetrievalFullContextToolOutput",
    "ThreadHistoryToolsRetrievalFullContextToolOutputToolResponse",
    "ThreadHistoryToolsRetrievalFullContextToolOutputToolResponseMetadata",
]


class ThreadHistoryToolsModelCitationTool(BaseModel):
    description: Optional[str] = None

    name: Optional[Literal["model_citation"]] = None

    tool_responses: Optional[Dict[str, List[str]]] = None


class ThreadHistoryToolsRetrievalChunkToolOutputToolResponseMetadata(BaseModel):
    chunk_doc_idx: int

    chunk_ext_id: str

    chunk_pg_idx: int

    created_at: str

    page_number: int

    chunk_id: Optional[str] = None

    doc_ext_id: Optional[str] = None

    doc_title: Optional[str] = None

    rerank_score: Optional[float] = None

    score: Optional[float] = None

    tokens: Optional[int] = None


class ThreadHistoryToolsRetrievalChunkToolOutputToolResponse(BaseModel):
    content: str

    metadata: ThreadHistoryToolsRetrievalChunkToolOutputToolResponseMetadata


class ThreadHistoryToolsRetrievalChunkToolOutput(BaseModel):
    description: Optional[str] = None

    name: Optional[Literal["retrieval_chunk"]] = None

    tool_args: Optional[Dict[str, List[str]]] = None

    tool_responses: Optional[Dict[str, List[ThreadHistoryToolsRetrievalChunkToolOutputToolResponse]]] = None


class ThreadHistoryToolsRetrievalFullContextToolOutputToolResponseMetadata(BaseModel):
    chunk_doc_idx: int

    chunk_ext_id: str

    chunk_pg_idx: int

    created_at: str

    page_number: int

    chunk_id: Optional[str] = None

    doc_ext_id: Optional[str] = None

    doc_title: Optional[str] = None

    rerank_score: Optional[float] = None

    score: Optional[float] = None

    tokens: Optional[int] = None


class ThreadHistoryToolsRetrievalFullContextToolOutputToolResponse(BaseModel):
    content: str

    metadata: ThreadHistoryToolsRetrievalFullContextToolOutputToolResponseMetadata


class ThreadHistoryToolsRetrievalFullContextToolOutput(BaseModel):
    description: Optional[str] = None

    name: Optional[Literal["retrieval_full_context"]] = None

    tool_args: Optional[Dict[str, List[str]]] = None

    tool_responses: Optional[Dict[str, List[ThreadHistoryToolsRetrievalFullContextToolOutputToolResponse]]] = None


ThreadHistoryTools: TypeAlias = Annotated[
    Union[
        ThreadHistoryToolsModelCitationTool,
        ThreadHistoryToolsRetrievalChunkToolOutput,
        ThreadHistoryToolsRetrievalFullContextToolOutput,
    ],
    PropertyInfo(discriminator="name"),
]


class ThreadHistory(BaseModel):
    content: str

    conversation_ext_id: str

    created_at: datetime

    created_by_ext_id: str

    external_id: str

    role: Literal["user", "assistant", "system"]

    configurations_name: Optional[str] = None

    parent_message_ext_id: Optional[str] = None

    shared: Optional[bool] = None

    tools: Optional[Dict[str, ThreadHistoryTools]] = None


class Thread(BaseModel):
    history: List[ThreadHistory]

    leaf_message_ext_id: str


class ConversationRetrieveThreadsResponse(BaseModel):
    conversation_ext_id: str

    threads: List[Thread]
