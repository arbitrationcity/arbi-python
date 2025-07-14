# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, List, Optional

from ..._models import BaseModel

__all__ = ["UserGetSettingsResponse"]


class UserGetSettingsResponse(BaseModel):
    last_workspace: Optional[str] = None

    pinned_workspaces: Optional[List[str]] = None

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
