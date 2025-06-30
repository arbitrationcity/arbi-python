# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

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
from ...types.api import AllConfigs, config_update_update_params
from ..._base_client import make_request_options
from ...types.api.all_configs import AllConfigs
from ...types.api.all_configs_param import AllConfigsParam
from ...types.api.config_update_update_response import ConfigUpdateUpdateResponse
from ...types.api.config_retrieve_schema_response import ConfigRetrieveSchemaResponse
from ...types.api.config_retrieve_versions_response import ConfigRetrieveVersionsResponse

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

    def retrieve(
        self,
        version: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AllConfigs:
        """
        Loads configurations from a specific .toml file version

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not version:
            raise ValueError(f"Expected a non-empty value for `version` but received {version!r}")
        return self._get(
            f"/api/configs/load/{version}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AllConfigs,
        )

    def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AllConfigs:
        """Return the current configurations for the user"""
        return self._get(
            "/api/configs/",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AllConfigs,
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
    ) -> ConfigRetrieveSchemaResponse:
        """Return the JSON schema for all config models"""
        return self._get(
            "/api/configs/schema",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConfigRetrieveSchemaResponse,
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
        """Returns a list of available configuration versions (.toml files)"""
        return self._get(
            "/api/configs/versions",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConfigRetrieveVersionsResponse,
        )

    def update_update(
        self,
        *,
        configs: AllConfigsParam,
        filename_suffix: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConfigUpdateUpdateResponse:
        """Update user-specific configuration settings.

        Saves new configurations to a TOML
        file if different from existing ones.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._put(
            "/api/configs/update",
            body=maybe_transform(
                {
                    "configs": configs,
                    "filename_suffix": filename_suffix,
                },
                config_update_update_params.ConfigUpdateUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConfigUpdateUpdateResponse,
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

    async def retrieve(
        self,
        version: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AllConfigs:
        """
        Loads configurations from a specific .toml file version

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not version:
            raise ValueError(f"Expected a non-empty value for `version` but received {version!r}")
        return await self._get(
            f"/api/configs/load/{version}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AllConfigs,
        )

    async def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AllConfigs:
        """Return the current configurations for the user"""
        return await self._get(
            "/api/configs/",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AllConfigs,
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
    ) -> ConfigRetrieveSchemaResponse:
        """Return the JSON schema for all config models"""
        return await self._get(
            "/api/configs/schema",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConfigRetrieveSchemaResponse,
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
        """Returns a list of available configuration versions (.toml files)"""
        return await self._get(
            "/api/configs/versions",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConfigRetrieveVersionsResponse,
        )

    async def update_update(
        self,
        *,
        configs: AllConfigsParam,
        filename_suffix: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConfigUpdateUpdateResponse:
        """Update user-specific configuration settings.

        Saves new configurations to a TOML
        file if different from existing ones.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._put(
            "/api/configs/update",
            body=await async_maybe_transform(
                {
                    "configs": configs,
                    "filename_suffix": filename_suffix,
                },
                config_update_update_params.ConfigUpdateUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConfigUpdateUpdateResponse,
        )


class ConfigsResourceWithRawResponse:
    def __init__(self, configs: ConfigsResource) -> None:
        self._configs = configs

        self.retrieve = to_raw_response_wrapper(
            configs.retrieve,
        )
        self.retrieve = to_raw_response_wrapper(
            configs.retrieve,
        )
        self.retrieve_schema = to_raw_response_wrapper(
            configs.retrieve_schema,
        )
        self.retrieve_versions = to_raw_response_wrapper(
            configs.retrieve_versions,
        )
        self.update_update = to_raw_response_wrapper(
            configs.update_update,
        )


class AsyncConfigsResourceWithRawResponse:
    def __init__(self, configs: AsyncConfigsResource) -> None:
        self._configs = configs

        self.retrieve = async_to_raw_response_wrapper(
            configs.retrieve,
        )
        self.retrieve = async_to_raw_response_wrapper(
            configs.retrieve,
        )
        self.retrieve_schema = async_to_raw_response_wrapper(
            configs.retrieve_schema,
        )
        self.retrieve_versions = async_to_raw_response_wrapper(
            configs.retrieve_versions,
        )
        self.update_update = async_to_raw_response_wrapper(
            configs.update_update,
        )


class ConfigsResourceWithStreamingResponse:
    def __init__(self, configs: ConfigsResource) -> None:
        self._configs = configs

        self.retrieve = to_streamed_response_wrapper(
            configs.retrieve,
        )
        self.retrieve = to_streamed_response_wrapper(
            configs.retrieve,
        )
        self.retrieve_schema = to_streamed_response_wrapper(
            configs.retrieve_schema,
        )
        self.retrieve_versions = to_streamed_response_wrapper(
            configs.retrieve_versions,
        )
        self.update_update = to_streamed_response_wrapper(
            configs.update_update,
        )


class AsyncConfigsResourceWithStreamingResponse:
    def __init__(self, configs: AsyncConfigsResource) -> None:
        self._configs = configs

        self.retrieve = async_to_streamed_response_wrapper(
            configs.retrieve,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            configs.retrieve,
        )
        self.retrieve_schema = async_to_streamed_response_wrapper(
            configs.retrieve_schema,
        )
        self.retrieve_versions = async_to_streamed_response_wrapper(
            configs.retrieve_versions,
        )
        self.update_update = async_to_streamed_response_wrapper(
            configs.update_update,
        )
