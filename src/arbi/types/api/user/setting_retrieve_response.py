# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Dict, List, Optional

from pydantic import Field as FieldInfo

from ...._models import BaseModel
from .user_active_config import UserActiveConfig

__all__ = ["SettingRetrieveResponse"]


class SettingRetrieveResponse(BaseModel):
    active_config: Optional[UserActiveConfig] = None
    """
    Partial configuration for user active config - all fields optional for
    overrides.
    """

    last_workspace: Optional[str] = None

    pinned_workspaces: Optional[List[str]] = None

    __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]
    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
