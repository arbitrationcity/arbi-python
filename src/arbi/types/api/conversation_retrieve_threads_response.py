# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["ConversationRetrieveThreadsResponse", "Thread", "ThreadHistory", "ThreadHistoryTools"]


class ThreadHistoryTools(BaseModel):
    description: str

    name: str

    tool_args: Dict[str, object]

    tool_responses: Optional[Dict[str, object]] = None


class ThreadHistory(BaseModel):
    content: str

    role: Literal["user", "assistant", "system"]

    configurations_name: Optional[str] = None

    created_at: Optional[datetime] = None

    external_id: Optional[str] = None

    parent_message_ext_id: Optional[str] = None

    shared: Optional[bool] = None

    tools: Optional[Dict[str, ThreadHistoryTools]] = None


class Thread(BaseModel):
    history: List[ThreadHistory]

    leaf_message_ext_id: str


class ConversationRetrieveThreadsResponse(BaseModel):
    conversation_ext_id: str

    threads: List[Thread]
