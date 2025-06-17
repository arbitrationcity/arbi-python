# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["SSOLoginResponse"]


class SSOLoginResponse(BaseModel):
    message: str

    user_ext_id: str

    passcode: Optional[str] = None
