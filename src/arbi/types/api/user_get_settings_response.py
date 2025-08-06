# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Dict, List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "UserGetSettingsResponse",
    "ActiveConfig",
    "ActiveConfigDocumentDateExtractorLlm",
    "ActiveConfigEmbedder",
    "ActiveConfigModelCitation",
    "ActiveConfigQueryLlm",
    "ActiveConfigReranker",
    "ActiveConfigRetriever",
    "ActiveConfigTitleLlm",
]


class ActiveConfigDocumentDateExtractorLlm(BaseModel):
    api_type: Optional[Literal["local", "remote"]] = FieldInfo(alias="API_TYPE", default=None)
    """API type for the model."""

    max_char_size_to_answer: Optional[int] = FieldInfo(alias="MAX_CHAR_SIZE_TO_ANSWER", default=None)
    """Maximum character size to answer."""

    max_tokens: Optional[int] = FieldInfo(alias="MAX_TOKENS", default=None)
    """Maximum number of tokens allowed."""

    api_model_name: Optional[str] = FieldInfo(alias="MODEL_NAME", default=None)
    """The name of the model to be used."""

    system_instruction: Optional[str] = FieldInfo(alias="SYSTEM_INSTRUCTION", default=None)

    temperature: Optional[float] = FieldInfo(alias="TEMPERATURE", default=None)
    """Temperature value for randomness."""


class ActiveConfigEmbedder(BaseModel):
    api_type: Optional[Literal["local", "remote"]] = FieldInfo(alias="API_TYPE", default=None)
    """The inference type (local or remote)."""

    api_model_name: Optional[str] = FieldInfo(alias="MODEL_NAME", default=None)
    """The name of the embedder model."""


class ActiveConfigModelCitation(BaseModel):
    api_model_name: Optional[str] = FieldInfo(alias="MODEL_NAME", default=None)
    """Name of the model to be used."""

    sim_threashold: Optional[float] = FieldInfo(alias="SIM_THREASHOLD", default=None)
    """How similar does the statement needs to be to be considered as citation."""


class ActiveConfigQueryLlm(BaseModel):
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


class ActiveConfigReranker(BaseModel):
    api_type: Optional[Literal["local", "remote"]] = FieldInfo(alias="API_TYPE", default=None)
    """The inference type (local or remote)."""

    max_numb_of_chunks: Optional[int] = FieldInfo(alias="MAX_NUMB_OF_CHUNKS", default=None)
    """Maximum number of chunks to return after reranking."""

    api_model_name: Optional[str] = FieldInfo(alias="MODEL_NAME", default=None)
    """Name of the reranking model to use."""


class ActiveConfigRetriever(BaseModel):
    group_size: Optional[int] = FieldInfo(alias="GROUP_SIZE", default=None)
    """Maximum number of chunks per document for retrieval."""

    max_distinct_documents: Optional[int] = FieldInfo(alias="MAX_DISTINCT_DOCUMENTS", default=None)
    """Maximum number of distinct documents to search for."""

    max_total_chunks_to_retrieve: Optional[int] = FieldInfo(alias="MAX_TOTAL_CHUNKS_TO_RETRIEVE", default=None)
    """Maximum total number of chunks to retrieve for all documents retrieved."""

    min_retrieval_sim_score: Optional[float] = FieldInfo(alias="MIN_RETRIEVAL_SIM_SCORE", default=None)
    """Minimum similarity score for retrieval of a chunk."""


class ActiveConfigTitleLlm(BaseModel):
    api_type: Optional[Literal["local", "remote"]] = FieldInfo(alias="API_TYPE", default=None)
    """API type for the model."""

    max_char_size_to_answer: Optional[int] = FieldInfo(alias="MAX_CHAR_SIZE_TO_ANSWER", default=None)
    """Maximum character size to answer."""

    max_tokens: Optional[int] = FieldInfo(alias="MAX_TOKENS", default=None)
    """Maximum number of tokens allowed."""

    api_model_name: Optional[str] = FieldInfo(alias="MODEL_NAME", default=None)
    """The name of the model to be used."""

    system_instruction: Optional[str] = FieldInfo(alias="SYSTEM_INSTRUCTION", default=None)

    temperature: Optional[float] = FieldInfo(alias="TEMPERATURE", default=None)
    """Temperature value for randomness."""


class ActiveConfig(BaseModel):
    chunker: Optional[object] = FieldInfo(alias="Chunker", default=None)

    document_date_extractor_llm: Optional[ActiveConfigDocumentDateExtractorLlm] = FieldInfo(
        alias="DocumentDateExtractorLLM", default=None
    )

    embedder: Optional[ActiveConfigEmbedder] = FieldInfo(alias="Embedder", default=None)

    api_model_citation: Optional[ActiveConfigModelCitation] = FieldInfo(alias="ModelCitation", default=None)

    parser: Optional[object] = FieldInfo(alias="Parser", default=None)

    query_llm: Optional[ActiveConfigQueryLlm] = FieldInfo(alias="QueryLLM", default=None)

    reranker: Optional[ActiveConfigReranker] = FieldInfo(alias="Reranker", default=None)

    retriever: Optional[ActiveConfigRetriever] = FieldInfo(alias="Retriever", default=None)

    title_llm: Optional[ActiveConfigTitleLlm] = FieldInfo(alias="TitleLLM", default=None)


class UserGetSettingsResponse(BaseModel):
    active_config: Optional[ActiveConfig] = None
    """
    Partial configuration for user active config - all fields optional for
    overrides.
    """

    last_workspace: Optional[str] = None

    pinned_workspaces: Optional[List[str]] = None

    __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]
    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
