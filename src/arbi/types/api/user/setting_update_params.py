# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import TypedDict

from .active_config_param import ActiveConfigParam

__all__ = ["SettingUpdateParams"]


class SettingUpdateParams(TypedDict, total=False):
    active_config: Optional[ActiveConfigParam]
    """
    Partial configuration for user active config - all fields optional for
    overrides.
    """

    pinned_workspaces: Optional[List[str]]
