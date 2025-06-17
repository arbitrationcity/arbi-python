# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["HealthRetrieveRemoteModelsResponse", "Model"]


class Model(BaseModel):
    model: str

    status: str

    details: Optional[str] = None


class HealthRetrieveRemoteModelsResponse(BaseModel):
    application: str

    models: List[Model]
