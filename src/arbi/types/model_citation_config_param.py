# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ModelCitationConfigParam"]


class ModelCitationConfigParam(TypedDict, total=False):
    model_name: Annotated[str, PropertyInfo(alias="MODEL_NAME")]
    """Name of the model to be used."""

    sim_threashold: Annotated[float, PropertyInfo(alias="SIM_THREASHOLD")]
    """How similar does the statement needs to be to be considered as citation."""
