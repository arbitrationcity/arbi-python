# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.api import (
    config_update_params,
)
from ..._base_client import make_request_options
from ...types.api.parser_config_param import ParserConfigParam
from ...types.api.chunker_config_param import ChunkerConfigParam
from ...types.api.embedder_config_param import EmbedderConfigParam
from ...types.api.reranker_config_param import RerankerConfigParam
from ...types.api.config_update_response import ConfigUpdateResponse
from ...types.api.query_llm_config_param import QueryLlmConfigParam
from ...types.api.retriever_config_param import RetrieverConfigParam
from ...types.api.title_llm_config_param import TitleLlmConfigParam
from ...types.api.model_citation_config_param import ModelCitationConfigParam
from ...types.api.config_retrieve_versions_response import ConfigRetrieveVersionsResponse
from ...types.api.document_date_extractor_llm_config_param import DocumentDateExtractorLlmConfigParam

__all__ = ["ConfigsResource", "AsyncConfigsResource"]


class ConfigsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ConfigsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/arbi-python#accessing-raw-response-data-eg-headers
        """
        return ConfigsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ConfigsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/arbi-python#with_streaming_response
        """
        return ConfigsResourceWithStreamingResponse(self)

    def update(
        self,
        *,
        chunker: Optional[ChunkerConfigParam] | NotGiven = NOT_GIVEN,
        document_date_extractor_llm: Optional[DocumentDateExtractorLlmConfigParam] | NotGiven = NOT_GIVEN,
        embedder: Optional[EmbedderConfigParam] | NotGiven = NOT_GIVEN,
        model_citation: Optional[ModelCitationConfigParam] | NotGiven = NOT_GIVEN,
        parent_message_ext_id: Optional[str] | NotGiven = NOT_GIVEN,
        parser: Optional[ParserConfigParam] | NotGiven = NOT_GIVEN,
        query_llm: Optional[QueryLlmConfigParam] | NotGiven = NOT_GIVEN,
        reranker: Optional[RerankerConfigParam] | NotGiven = NOT_GIVEN,
        retriever: Optional[RetrieverConfigParam] | NotGiven = NOT_GIVEN,
        title: str | NotGiven = NOT_GIVEN,
        title_llm: Optional[TitleLlmConfigParam] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConfigUpdateResponse:
        """
        Save a new configuration.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/configs/",
            body=maybe_transform(
                {
                    "chunker": chunker,
                    "document_date_extractor_llm": document_date_extractor_llm,
                    "embedder": embedder,
                    "model_citation": model_citation,
                    "parent_message_ext_id": parent_message_ext_id,
                    "parser": parser,
                    "query_llm": query_llm,
                    "reranker": reranker,
                    "retriever": retriever,
                    "title": title,
                    "title_llm": title_llm,
                },
                config_update_params.ConfigUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConfigUpdateResponse,
        )

    def retrieve_schema(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """Return the JSON schema for all config models"""
        return self._get(
            "/api/configs/schema",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def retrieve_versions(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConfigRetrieveVersionsResponse:
        """Returns a list of available configuration versions for the current user"""
        return self._get(
            "/api/configs/versions",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConfigRetrieveVersionsResponse,
        )


class AsyncConfigsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncConfigsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/arbi-python#accessing-raw-response-data-eg-headers
        """
        return AsyncConfigsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncConfigsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/arbi-python#with_streaming_response
        """
        return AsyncConfigsResourceWithStreamingResponse(self)

    async def update(
        self,
        *,
        chunker: Optional[ChunkerConfigParam] | NotGiven = NOT_GIVEN,
        document_date_extractor_llm: Optional[DocumentDateExtractorLlmConfigParam] | NotGiven = NOT_GIVEN,
        embedder: Optional[EmbedderConfigParam] | NotGiven = NOT_GIVEN,
        model_citation: Optional[ModelCitationConfigParam] | NotGiven = NOT_GIVEN,
        parent_message_ext_id: Optional[str] | NotGiven = NOT_GIVEN,
        parser: Optional[ParserConfigParam] | NotGiven = NOT_GIVEN,
        query_llm: Optional[QueryLlmConfigParam] | NotGiven = NOT_GIVEN,
        reranker: Optional[RerankerConfigParam] | NotGiven = NOT_GIVEN,
        retriever: Optional[RetrieverConfigParam] | NotGiven = NOT_GIVEN,
        title: str | NotGiven = NOT_GIVEN,
        title_llm: Optional[TitleLlmConfigParam] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConfigUpdateResponse:
        """
        Save a new configuration.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/configs/",
            body=await async_maybe_transform(
                {
                    "chunker": chunker,
                    "document_date_extractor_llm": document_date_extractor_llm,
                    "embedder": embedder,
                    "model_citation": model_citation,
                    "parent_message_ext_id": parent_message_ext_id,
                    "parser": parser,
                    "query_llm": query_llm,
                    "reranker": reranker,
                    "retriever": retriever,
                    "title": title,
                    "title_llm": title_llm,
                },
                config_update_params.ConfigUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConfigUpdateResponse,
        )

    async def retrieve_schema(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """Return the JSON schema for all config models"""
        return await self._get(
            "/api/configs/schema",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def retrieve_versions(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConfigRetrieveVersionsResponse:
        """Returns a list of available configuration versions for the current user"""
        return await self._get(
            "/api/configs/versions",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConfigRetrieveVersionsResponse,
        )


class ConfigsResourceWithRawResponse:
    def __init__(self, configs: ConfigsResource) -> None:
        self._configs = configs

        self.update = to_raw_response_wrapper(
            configs.update,
        )
        self.retrieve_schema = to_raw_response_wrapper(
            configs.retrieve_schema,
        )
        self.retrieve_versions = to_raw_response_wrapper(
            configs.retrieve_versions,
        )


class AsyncConfigsResourceWithRawResponse:
    def __init__(self, configs: AsyncConfigsResource) -> None:
        self._configs = configs

        self.update = async_to_raw_response_wrapper(
            configs.update,
        )
        self.retrieve_schema = async_to_raw_response_wrapper(
            configs.retrieve_schema,
        )
        self.retrieve_versions = async_to_raw_response_wrapper(
            configs.retrieve_versions,
        )


class ConfigsResourceWithStreamingResponse:
    def __init__(self, configs: ConfigsResource) -> None:
        self._configs = configs

        self.update = to_streamed_response_wrapper(
            configs.update,
        )
        self.retrieve_schema = to_streamed_response_wrapper(
            configs.retrieve_schema,
        )
        self.retrieve_versions = to_streamed_response_wrapper(
            configs.retrieve_versions,
        )


class AsyncConfigsResourceWithStreamingResponse:
    def __init__(self, configs: AsyncConfigsResource) -> None:
        self._configs = configs

        self.update = async_to_streamed_response_wrapper(
            configs.update,
        )
        self.retrieve_schema = async_to_streamed_response_wrapper(
            configs.retrieve_schema,
        )
        self.retrieve_versions = async_to_streamed_response_wrapper(
            configs.retrieve_versions,
        )
