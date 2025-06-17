# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["SSORotatePasscodeResponse"]


class SSORotatePasscodeResponse(BaseModel):
    message: str

    new_passcode: str
