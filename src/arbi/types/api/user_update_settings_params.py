# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = [
    "UserUpdateSettingsParams",
    "ActiveConfig",
    "ActiveConfigDocumentDateExtractorLlm",
    "ActiveConfigEmbedder",
    "ActiveConfigModelCitation",
    "ActiveConfigQueryLlm",
    "ActiveConfigReranker",
    "ActiveConfigRetriever",
    "ActiveConfigTitleLlm",
]


class UserUpdateSettingsParams(TypedDict, total=False):
    active_config: Optional[ActiveConfig]
    """
    Partial configuration for user active config - all fields optional for
    overrides.
    """

    pinned_workspaces: Optional[List[str]]


class ActiveConfigDocumentDateExtractorLlm(TypedDict, total=False):
    api_type: Annotated[Literal["local", "remote"], PropertyInfo(alias="API_TYPE")]
    """API type for the model."""

    max_char_size_to_answer: Annotated[int, PropertyInfo(alias="MAX_CHAR_SIZE_TO_ANSWER")]
    """Maximum character size to answer."""

    max_tokens: Annotated[int, PropertyInfo(alias="MAX_TOKENS")]
    """Maximum number of tokens allowed."""

    model_name: Annotated[str, PropertyInfo(alias="MODEL_NAME")]
    """The name of the model to be used."""

    system_instruction: Annotated[str, PropertyInfo(alias="SYSTEM_INSTRUCTION")]

    temperature: Annotated[float, PropertyInfo(alias="TEMPERATURE")]
    """Temperature value for randomness."""


class ActiveConfigEmbedder(TypedDict, total=False):
    api_type: Annotated[Literal["local", "remote"], PropertyInfo(alias="API_TYPE")]
    """The inference type (local or remote)."""

    model_name: Annotated[str, PropertyInfo(alias="MODEL_NAME")]
    """The name of the embedder model."""


class ActiveConfigModelCitation(TypedDict, total=False):
    model_name: Annotated[str, PropertyInfo(alias="MODEL_NAME")]
    """Name of the model to be used."""

    sim_threashold: Annotated[float, PropertyInfo(alias="SIM_THREASHOLD")]
    """How similar does the statement needs to be to be considered as citation."""


class ActiveConfigQueryLlm(TypedDict, total=False):
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


class ActiveConfigReranker(TypedDict, total=False):
    api_type: Annotated[Literal["local", "remote"], PropertyInfo(alias="API_TYPE")]
    """The inference type (local or remote)."""

    max_numb_of_chunks: Annotated[int, PropertyInfo(alias="MAX_NUMB_OF_CHUNKS")]
    """Maximum number of chunks to return after reranking."""

    model_name: Annotated[str, PropertyInfo(alias="MODEL_NAME")]
    """Name of the reranking model to use."""


class ActiveConfigRetriever(TypedDict, total=False):
    group_size: Annotated[int, PropertyInfo(alias="GROUP_SIZE")]
    """Maximum number of chunks per document for retrieval."""

    max_distinct_documents: Annotated[int, PropertyInfo(alias="MAX_DISTINCT_DOCUMENTS")]
    """Maximum number of distinct documents to search for."""

    max_total_chunks_to_retrieve: Annotated[int, PropertyInfo(alias="MAX_TOTAL_CHUNKS_TO_RETRIEVE")]
    """Maximum total number of chunks to retrieve for all documents retrieved."""

    min_retrieval_sim_score: Annotated[float, PropertyInfo(alias="MIN_RETRIEVAL_SIM_SCORE")]
    """Minimum similarity score for retrieval of a chunk."""


class ActiveConfigTitleLlm(TypedDict, total=False):
    api_type: Annotated[Literal["local", "remote"], PropertyInfo(alias="API_TYPE")]
    """API type for the model."""

    max_char_size_to_answer: Annotated[int, PropertyInfo(alias="MAX_CHAR_SIZE_TO_ANSWER")]
    """Maximum character size to answer."""

    max_tokens: Annotated[int, PropertyInfo(alias="MAX_TOKENS")]
    """Maximum number of tokens allowed."""

    model_name: Annotated[str, PropertyInfo(alias="MODEL_NAME")]
    """The name of the model to be used."""

    system_instruction: Annotated[str, PropertyInfo(alias="SYSTEM_INSTRUCTION")]

    temperature: Annotated[float, PropertyInfo(alias="TEMPERATURE")]
    """Temperature value for randomness."""


class ActiveConfig(TypedDict, total=False):
    chunker: Annotated[Optional[object], PropertyInfo(alias="Chunker")]

    document_date_extractor_llm: Annotated[
        Optional[ActiveConfigDocumentDateExtractorLlm], PropertyInfo(alias="DocumentDateExtractorLLM")
    ]

    embedder: Annotated[Optional[ActiveConfigEmbedder], PropertyInfo(alias="Embedder")]

    model_citation: Annotated[Optional[ActiveConfigModelCitation], PropertyInfo(alias="ModelCitation")]

    parser: Annotated[Optional[object], PropertyInfo(alias="Parser")]

    query_llm: Annotated[Optional[ActiveConfigQueryLlm], PropertyInfo(alias="QueryLLM")]

    reranker: Annotated[Optional[ActiveConfigReranker], PropertyInfo(alias="Reranker")]

    retriever: Annotated[Optional[ActiveConfigRetriever], PropertyInfo(alias="Retriever")]

    title_llm: Annotated[Optional[ActiveConfigTitleLlm], PropertyInfo(alias="TitleLLM")]
