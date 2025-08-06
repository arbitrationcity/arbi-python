# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ModelCitationConfig"]


class ModelCitationConfig(BaseModel):
    api_model_name: Optional[str] = FieldInfo(alias="MODEL_NAME", default=None)
    """Name of the model to be used."""

    sim_threashold: Optional[float] = FieldInfo(alias="SIM_THREASHOLD", default=None)
    """How similar does the statement needs to be to be considered as citation."""
