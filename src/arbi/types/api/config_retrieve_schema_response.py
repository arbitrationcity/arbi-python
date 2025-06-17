# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ConfigRetrieveSchemaResponse"]


class ConfigRetrieveSchemaResponse(BaseModel):
    chunker: Dict[str, object] = FieldInfo(alias="Chunker")

    embedder: Dict[str, object] = FieldInfo(alias="Embedder")

    api_model_citation: Dict[str, object] = FieldInfo(alias="ModelCitation")

    parser: Dict[str, object] = FieldInfo(alias="Parser")

    query_llm: Dict[str, object] = FieldInfo(alias="QueryLLM")

    reranker: Dict[str, object] = FieldInfo(alias="Reranker")

    retriever: Dict[str, object] = FieldInfo(alias="Retriever")

    title_llm: Dict[str, object] = FieldInfo(alias="TitleLLM")
