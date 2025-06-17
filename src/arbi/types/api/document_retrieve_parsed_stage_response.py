# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from ..._models import BaseModel

__all__ = ["DocumentRetrieveParsedStageResponse", "Metadata", "Chunk", "ChunkMetadata"]


class Metadata(BaseModel):
    doc_ext_id: Optional[str] = None

    file_name: Optional[str] = None

    re_ocred: Optional[bool] = None

    total_number_of_pages: Optional[int] = None


class ChunkMetadata(BaseModel):
    chunk_doc_idx: int

    chunk_ext_id: str

    chunk_pg_idx: int

    created_at: str

    page_number: int

    chunk_id: Optional[str] = None

    doc_ext_id: Optional[str] = None

    doc_title: Optional[str] = None

    rerank_score: Optional[float] = None

    score: Optional[float] = None


class Chunk(BaseModel):
    content: str

    metadata: ChunkMetadata


class DocumentRetrieveParsedStageResponse(BaseModel):
    metadata: Metadata

    chunks: Optional[List[Chunk]] = None

    footnotes: Optional[Dict[str, str]] = None
