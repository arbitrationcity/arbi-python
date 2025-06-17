# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["SSOInviteResponse"]


class SSOInviteResponse(BaseModel):
    message: str

    user_ext_id: str
