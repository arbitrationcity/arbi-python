# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["AssistantCreateCitationsParams"]


class AssistantCreateCitationsParams(TypedDict, total=False):
    message_id: Required[str]
