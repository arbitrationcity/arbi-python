# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from ..._models import BaseModel

__all__ = ["WorkspaceListUsersResponse", "WorkspaceListUsersResponseItem"]


class WorkspaceListUsersResponseItem(BaseModel):
    user_email: str

    user_ext_id: str


WorkspaceListUsersResponse: TypeAlias = List[WorkspaceListUsersResponseItem]
