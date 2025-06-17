# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = [
    "AllConfigsParam",
    "DocumentDateExtractorLlm",
    "Embedder",
    "ModelCitation",
    "QueryLlm",
    "Reranker",
    "Retriever",
    "TitleLlm",
]


class DocumentDateExtractorLlm(TypedDict, total=False):
    api_type: Annotated[Literal["local", "remote"], PropertyInfo(alias="API_TYPE")]
    """The inference type (local or remote)."""

    max_char_size_to_answer: Annotated[int, PropertyInfo(alias="MAX_CHAR_SIZE_TO_ANSWER")]
    """Maximum character size to answer."""

    max_tokens: Annotated[int, PropertyInfo(alias="MAX_TOKENS")]
    """Maximum number of tokens allowed."""

    model_name: Annotated[str, PropertyInfo(alias="MODEL_NAME")]
    """The name of the model to be used."""

    system_instruction: Annotated[str, PropertyInfo(alias="SYSTEM_INSTRUCTION")]

    temperature: Annotated[float, PropertyInfo(alias="TEMPERATURE")]
    """Temperature value for randomness."""


class Embedder(TypedDict, total=False):
    api_type: Annotated[Literal["local", "remote"], PropertyInfo(alias="API_TYPE")]
    """The inference type (local or remote)."""

    model_name: Annotated[str, PropertyInfo(alias="MODEL_NAME")]
    """The name of the embedder model."""


class ModelCitation(TypedDict, total=False):
    sim_threashold: Annotated[float, PropertyInfo(alias="SIM_THREASHOLD")]
    """How similar does the statement needs to be to be considered as citation."""


class QueryLlm(TypedDict, total=False):
    api_type: Annotated[Literal["local", "remote"], PropertyInfo(alias="API_TYPE")]
    """The inference type (local or remote)."""

    max_char_size_to_answer: Annotated[int, PropertyInfo(alias="MAX_CHAR_SIZE_TO_ANSWER")]
    """Maximum character size to answer."""

    max_tokens: Annotated[int, PropertyInfo(alias="MAX_TOKENS")]
    """Maximum number of tokens allowed."""

    model_name: Annotated[str, PropertyInfo(alias="MODEL_NAME")]
    """The name of the model to be used."""

    system_instruction: Annotated[str, PropertyInfo(alias="SYSTEM_INSTRUCTION")]
    """The system instruction string."""

    temperature: Annotated[float, PropertyInfo(alias="TEMPERATURE")]
    """Temperature value for randomness."""


class Reranker(TypedDict, total=False):
    api_type: Annotated[Literal["local", "remote"], PropertyInfo(alias="API_TYPE")]
    """The inference type (local or remote)."""

    max_numb_of_chunks: Annotated[int, PropertyInfo(alias="MAX_NUMB_OF_CHUNKS")]
    """Maximum number of chunks to return after reranking."""

    model_name: Annotated[str, PropertyInfo(alias="MODEL_NAME")]
    """Name of the reranking model to use."""


class Retriever(TypedDict, total=False):
    group_size: Annotated[int, PropertyInfo(alias="GROUP_SIZE")]
    """Maximum number of chunks per document for retrieval."""

    max_distinct_documents: Annotated[int, PropertyInfo(alias="MAX_DISTINCT_DOCUMENTS")]
    """Maximum number of distinct documents to search for."""

    max_total_chunks_to_retrieve: Annotated[int, PropertyInfo(alias="MAX_TOTAL_CHUNKS_TO_RETRIEVE")]
    """Maximum total number of chunks to retrieve for all documents retrieved."""

    min_retrieval_sim_score: Annotated[float, PropertyInfo(alias="MIN_RETRIEVAL_SIM_SCORE")]
    """Minimum similarity score for retrieval of a chunk."""


class TitleLlm(TypedDict, total=False):
    api_type: Annotated[Literal["local", "remote"], PropertyInfo(alias="API_TYPE")]
    """The inference type (local or remote)."""

    max_char_size_to_answer: Annotated[int, PropertyInfo(alias="MAX_CHAR_SIZE_TO_ANSWER")]
    """Maximum character size to answer."""

    max_tokens: Annotated[int, PropertyInfo(alias="MAX_TOKENS")]
    """Maximum number of tokens allowed."""

    model_name: Annotated[str, PropertyInfo(alias="MODEL_NAME")]
    """The name of the model to be used."""

    system_instruction: Annotated[str, PropertyInfo(alias="SYSTEM_INSTRUCTION")]

    temperature: Annotated[float, PropertyInfo(alias="TEMPERATURE")]
    """Temperature value for randomness."""


class AllConfigsParam(TypedDict, total=False):
    chunker: Annotated[object, PropertyInfo(alias="Chunker")]

    document_date_extractor_llm: Annotated[DocumentDateExtractorLlm, PropertyInfo(alias="DocumentDateExtractorLLM")]

    embedder: Annotated[Embedder, PropertyInfo(alias="Embedder")]

    model_citation: Annotated[ModelCitation, PropertyInfo(alias="ModelCitation")]

    parser: Annotated[object, PropertyInfo(alias="Parser")]

    query_llm: Annotated[QueryLlm, PropertyInfo(alias="QueryLLM")]

    reranker: Annotated[Reranker, PropertyInfo(alias="Reranker")]

    retriever: Annotated[Retriever, PropertyInfo(alias="Retriever")]

    title_llm: Annotated[TitleLlm, PropertyInfo(alias="TitleLLM")]
