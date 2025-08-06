# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.api.health_retrieve_app_response import HealthRetrieveAppResponse
from ...types.api.health_retrieve_models_response import HealthRetrieveModelsResponse
from ...types.api.health_retrieve_services_response import HealthRetrieveServicesResponse
from ...types.api.health_retrieve_remote_models_response import HealthRetrieveRemoteModelsResponse

__all__ = ["HealthResource", "AsyncHealthResource"]


class HealthResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> HealthResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/arbi-python#accessing-raw-response-data-eg-headers
        """
        return HealthResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> HealthResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/arbi-python#with_streaming_response
        """
        return HealthResourceWithStreamingResponse(self)

    def retrieve_app(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> HealthRetrieveAppResponse:
        """Lightweight health check endpoint for the arbi-app itself."""
        return self._get(
            "/api/health/app",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=HealthRetrieveAppResponse,
        )

    def retrieve_models(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> HealthRetrieveModelsResponse:
        """Returns available models with model_name and api_type fields"""
        return self._get(
            "/api/health/models",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=HealthRetrieveModelsResponse,
        )

    def retrieve_remote_models(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> HealthRetrieveRemoteModelsResponse:
        """
        Endpoint to check the health of various models hosted on the LiteLLM platform.
        This endpoint fetches a list of available models and checks if each one is
        operational.
        """
        return self._get(
            "/api/health/remote-models",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=HealthRetrieveRemoteModelsResponse,
        )

    def retrieve_services(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> HealthRetrieveServicesResponse:
        """
        Health check endpoint that verifies the status of the application and external
        services. Always returns a structured object with the health status of all
        services.
        """
        return self._get(
            "/api/health/services",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=HealthRetrieveServicesResponse,
        )


class AsyncHealthResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncHealthResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/arbi-python#accessing-raw-response-data-eg-headers
        """
        return AsyncHealthResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncHealthResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/arbi-python#with_streaming_response
        """
        return AsyncHealthResourceWithStreamingResponse(self)

    async def retrieve_app(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> HealthRetrieveAppResponse:
        """Lightweight health check endpoint for the arbi-app itself."""
        return await self._get(
            "/api/health/app",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=HealthRetrieveAppResponse,
        )

    async def retrieve_models(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> HealthRetrieveModelsResponse:
        """Returns available models with model_name and api_type fields"""
        return await self._get(
            "/api/health/models",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=HealthRetrieveModelsResponse,
        )

    async def retrieve_remote_models(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> HealthRetrieveRemoteModelsResponse:
        """
        Endpoint to check the health of various models hosted on the LiteLLM platform.
        This endpoint fetches a list of available models and checks if each one is
        operational.
        """
        return await self._get(
            "/api/health/remote-models",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=HealthRetrieveRemoteModelsResponse,
        )

    async def retrieve_services(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> HealthRetrieveServicesResponse:
        """
        Health check endpoint that verifies the status of the application and external
        services. Always returns a structured object with the health status of all
        services.
        """
        return await self._get(
            "/api/health/services",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=HealthRetrieveServicesResponse,
        )


class HealthResourceWithRawResponse:
    def __init__(self, health: HealthResource) -> None:
        self._health = health

        self.retrieve_app = to_raw_response_wrapper(
            health.retrieve_app,
        )
        self.retrieve_models = to_raw_response_wrapper(
            health.retrieve_models,
        )
        self.retrieve_remote_models = to_raw_response_wrapper(
            health.retrieve_remote_models,
        )
        self.retrieve_services = to_raw_response_wrapper(
            health.retrieve_services,
        )


class AsyncHealthResourceWithRawResponse:
    def __init__(self, health: AsyncHealthResource) -> None:
        self._health = health

        self.retrieve_app = async_to_raw_response_wrapper(
            health.retrieve_app,
        )
        self.retrieve_models = async_to_raw_response_wrapper(
            health.retrieve_models,
        )
        self.retrieve_remote_models = async_to_raw_response_wrapper(
            health.retrieve_remote_models,
        )
        self.retrieve_services = async_to_raw_response_wrapper(
            health.retrieve_services,
        )


class HealthResourceWithStreamingResponse:
    def __init__(self, health: HealthResource) -> None:
        self._health = health

        self.retrieve_app = to_streamed_response_wrapper(
            health.retrieve_app,
        )
        self.retrieve_models = to_streamed_response_wrapper(
            health.retrieve_models,
        )
        self.retrieve_remote_models = to_streamed_response_wrapper(
            health.retrieve_remote_models,
        )
        self.retrieve_services = to_streamed_response_wrapper(
            health.retrieve_services,
        )


class AsyncHealthResourceWithStreamingResponse:
    def __init__(self, health: AsyncHealthResource) -> None:
        self._health = health

        self.retrieve_app = async_to_streamed_response_wrapper(
            health.retrieve_app,
        )
        self.retrieve_models = async_to_streamed_response_wrapper(
            health.retrieve_models,
        )
        self.retrieve_remote_models = async_to_streamed_response_wrapper(
            health.retrieve_remote_models,
        )
        self.retrieve_services = async_to_streamed_response_wrapper(
            health.retrieve_services,
        )
