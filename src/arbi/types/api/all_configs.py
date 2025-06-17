# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "AllConfigs",
    "DocumentDateExtractorLlm",
    "Embedder",
    "ModelCitation",
    "QueryLlm",
    "Reranker",
    "Retriever",
    "TitleLlm",
]


class DocumentDateExtractorLlm(BaseModel):
    api_type: Optional[Literal["local", "remote"]] = FieldInfo(alias="API_TYPE", default=None)
    """The inference type (local or remote)."""

    max_char_size_to_answer: Optional[int] = FieldInfo(alias="MAX_CHAR_SIZE_TO_ANSWER", default=None)
    """Maximum character size to answer."""

    max_tokens: Optional[int] = FieldInfo(alias="MAX_TOKENS", default=None)
    """Maximum number of tokens allowed."""

    api_model_name: Optional[str] = FieldInfo(alias="MODEL_NAME", default=None)
    """The name of the model to be used."""

    system_instruction: Optional[str] = FieldInfo(alias="SYSTEM_INSTRUCTION", default=None)

    temperature: Optional[float] = FieldInfo(alias="TEMPERATURE", default=None)
    """Temperature value for randomness."""


class Embedder(BaseModel):
    api_type: Optional[Literal["local", "remote"]] = FieldInfo(alias="API_TYPE", default=None)
    """The inference type (local or remote)."""

    api_model_name: Optional[str] = FieldInfo(alias="MODEL_NAME", default=None)
    """The name of the embedder model."""


class ModelCitation(BaseModel):
    sim_threashold: Optional[float] = FieldInfo(alias="SIM_THREASHOLD", default=None)
    """How similar does the statement needs to be to be considered as citation."""


class QueryLlm(BaseModel):
    api_type: Optional[Literal["local", "remote"]] = FieldInfo(alias="API_TYPE", default=None)
    """The inference type (local or remote)."""

    max_char_size_to_answer: Optional[int] = FieldInfo(alias="MAX_CHAR_SIZE_TO_ANSWER", default=None)
    """Maximum character size to answer."""

    max_tokens: Optional[int] = FieldInfo(alias="MAX_TOKENS", default=None)
    """Maximum number of tokens allowed."""

    api_model_name: Optional[str] = FieldInfo(alias="MODEL_NAME", default=None)
    """The name of the model to be used."""

    system_instruction: Optional[str] = FieldInfo(alias="SYSTEM_INSTRUCTION", default=None)
    """The system instruction string."""

    temperature: Optional[float] = FieldInfo(alias="TEMPERATURE", default=None)
    """Temperature value for randomness."""


class Reranker(BaseModel):
    api_type: Optional[Literal["local", "remote"]] = FieldInfo(alias="API_TYPE", default=None)
    """The inference type (local or remote)."""

    max_numb_of_chunks: Optional[int] = FieldInfo(alias="MAX_NUMB_OF_CHUNKS", default=None)
    """Maximum number of chunks to return after reranking."""

    api_model_name: Optional[str] = FieldInfo(alias="MODEL_NAME", default=None)
    """Name of the reranking model to use."""


class Retriever(BaseModel):
    group_size: Optional[int] = FieldInfo(alias="GROUP_SIZE", default=None)
    """Maximum number of chunks per document for retrieval."""

    max_distinct_documents: Optional[int] = FieldInfo(alias="MAX_DISTINCT_DOCUMENTS", default=None)
    """Maximum number of distinct documents to search for."""

    max_total_chunks_to_retrieve: Optional[int] = FieldInfo(alias="MAX_TOTAL_CHUNKS_TO_RETRIEVE", default=None)
    """Maximum total number of chunks to retrieve for all documents retrieved."""

    min_retrieval_sim_score: Optional[float] = FieldInfo(alias="MIN_RETRIEVAL_SIM_SCORE", default=None)
    """Minimum similarity score for retrieval of a chunk."""


class TitleLlm(BaseModel):
    api_type: Optional[Literal["local", "remote"]] = FieldInfo(alias="API_TYPE", default=None)
    """The inference type (local or remote)."""

    max_char_size_to_answer: Optional[int] = FieldInfo(alias="MAX_CHAR_SIZE_TO_ANSWER", default=None)
    """Maximum character size to answer."""

    max_tokens: Optional[int] = FieldInfo(alias="MAX_TOKENS", default=None)
    """Maximum number of tokens allowed."""

    api_model_name: Optional[str] = FieldInfo(alias="MODEL_NAME", default=None)
    """The name of the model to be used."""

    system_instruction: Optional[str] = FieldInfo(alias="SYSTEM_INSTRUCTION", default=None)

    temperature: Optional[float] = FieldInfo(alias="TEMPERATURE", default=None)
    """Temperature value for randomness."""


class AllConfigs(BaseModel):
    chunker: Optional[object] = FieldInfo(alias="Chunker", default=None)

    document_date_extractor_llm: Optional[DocumentDateExtractorLlm] = FieldInfo(
        alias="DocumentDateExtractorLLM", default=None
    )

    embedder: Optional[Embedder] = FieldInfo(alias="Embedder", default=None)

    api_model_citation: Optional[ModelCitation] = FieldInfo(alias="ModelCitation", default=None)

    parser: Optional[object] = FieldInfo(alias="Parser", default=None)

    query_llm: Optional[QueryLlm] = FieldInfo(alias="QueryLLM", default=None)

    reranker: Optional[Reranker] = FieldInfo(alias="Reranker", default=None)

    retriever: Optional[Retriever] = FieldInfo(alias="Retriever", default=None)

    title_llm: Optional[TitleLlm] = FieldInfo(alias="TitleLLM", default=None)
