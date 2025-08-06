# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["HealthRetrieveModelsResponse", "Model"]


class Model(BaseModel):
    api_type: str

    api_model_name: str = FieldInfo(alias="model_name")


class HealthRetrieveModelsResponse(BaseModel):
    models: List[Model]
