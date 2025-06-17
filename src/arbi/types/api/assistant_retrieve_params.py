# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Required, TypedDict

__all__ = ["AssistantRetrieveParams", "Tools"]


class AssistantRetrieveParams(TypedDict, total=False):
    content: Required[str]

    workspace_ext_id: Required[str]

    model: Optional[str]

    parent_message_ext_id: Optional[str]

    system_message: Optional[str]

    tools: Dict[str, Tools]


class Tools(TypedDict, total=False):
    description: Required[str]

    name: Required[str]

    tool_args: Required[Dict[str, object]]

    tool_responses: Dict[str, object]
