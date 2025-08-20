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
from ...types.api.simple_response import SimpleResponse

__all__ = ["TestResource", "AsyncTestResource"]


class TestResource(SyncAPIResource):
    __test__ = False

    @cached_property
    def with_raw_response(self) -> TestResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/arbitrationcity/arbi-python#accessing-raw-response-data-eg-headers
        """
        return TestResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TestResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/arbitrationcity/arbi-python#with_streaming_response
        """
        return TestResourceWithStreamingResponse(self)

    def test_endpoint_1(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SimpleResponse:
        """Test Endpoint 1"""
        return self._get(
            "/api/test/endpoint-1",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimpleResponse,
        )

    def test_endpoint_10(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SimpleResponse:
        """Test Endpoint 10"""
        return self._get(
            "/api/test/endpoint-10",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimpleResponse,
        )

    def test_endpoint_11(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SimpleResponse:
        """Test Endpoint 11"""
        return self._get(
            "/api/test/endpoint-11",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimpleResponse,
        )

    def test_endpoint_12(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SimpleResponse:
        """Test Endpoint 12"""
        return self._get(
            "/api/test/endpoint-12",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimpleResponse,
        )

    def test_endpoint_13(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SimpleResponse:
        """Test Endpoint 13"""
        return self._get(
            "/api/test/endpoint-13",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimpleResponse,
        )

    def test_endpoint_14(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SimpleResponse:
        """Test Endpoint 14"""
        return self._get(
            "/api/test/endpoint-14",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimpleResponse,
        )

    def test_endpoint_15(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SimpleResponse:
        """Test Endpoint 15"""
        return self._get(
            "/api/test/endpoint-15",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimpleResponse,
        )

    def test_endpoint_16(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SimpleResponse:
        """Test Endpoint 16"""
        return self._get(
            "/api/test/endpoint-16",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimpleResponse,
        )

    def test_endpoint_17(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SimpleResponse:
        """Test Endpoint 17"""
        return self._get(
            "/api/test/endpoint-17",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimpleResponse,
        )

    def test_endpoint_18(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SimpleResponse:
        """Test Endpoint 18"""
        return self._get(
            "/api/test/endpoint-18",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimpleResponse,
        )

    def test_endpoint_19(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SimpleResponse:
        """Test Endpoint 19"""
        return self._get(
            "/api/test/endpoint-19",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimpleResponse,
        )

    def test_endpoint_2(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SimpleResponse:
        """Test Endpoint 2"""
        return self._get(
            "/api/test/endpoint-2",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimpleResponse,
        )

    def test_endpoint_20(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SimpleResponse:
        """Test Endpoint 20"""
        return self._get(
            "/api/test/endpoint-20",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimpleResponse,
        )

    def test_endpoint_21(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SimpleResponse:
        """Test Endpoint 21"""
        return self._get(
            "/api/test/endpoint-21",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimpleResponse,
        )

    def test_endpoint_22(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SimpleResponse:
        """Test Endpoint 22"""
        return self._get(
            "/api/test/endpoint-22",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimpleResponse,
        )

    def test_endpoint_23(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SimpleResponse:
        """Test Endpoint 23"""
        return self._get(
            "/api/test/endpoint-23",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimpleResponse,
        )

    def test_endpoint_24(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SimpleResponse:
        """Test Endpoint 24"""
        return self._get(
            "/api/test/endpoint-24",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimpleResponse,
        )

    def test_endpoint_25(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SimpleResponse:
        """Test Endpoint 25"""
        return self._get(
            "/api/test/endpoint-25",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimpleResponse,
        )

    def test_endpoint_26(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SimpleResponse:
        """Test Endpoint 26"""
        return self._get(
            "/api/test/endpoint-26",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimpleResponse,
        )

    def test_endpoint_27(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SimpleResponse:
        """Test Endpoint 27"""
        return self._get(
            "/api/test/endpoint-27",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimpleResponse,
        )

    def test_endpoint_28(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SimpleResponse:
        """Test Endpoint 28"""
        return self._get(
            "/api/test/endpoint-28",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimpleResponse,
        )

    def test_endpoint_29(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SimpleResponse:
        """Test Endpoint 29"""
        return self._get(
            "/api/test/endpoint-29",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimpleResponse,
        )

    def test_endpoint_3(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SimpleResponse:
        """Test Endpoint 3"""
        return self._get(
            "/api/test/endpoint-3",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimpleResponse,
        )

    def test_endpoint_30(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SimpleResponse:
        """Test Endpoint 30"""
        return self._get(
            "/api/test/endpoint-30",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimpleResponse,
        )

    def test_endpoint_4(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SimpleResponse:
        """Test Endpoint 4"""
        return self._get(
            "/api/test/endpoint-4",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimpleResponse,
        )

    def test_endpoint_5(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SimpleResponse:
        """Test Endpoint 5"""
        return self._get(
            "/api/test/endpoint-5",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimpleResponse,
        )

    def test_endpoint_6(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SimpleResponse:
        """Test Endpoint 6"""
        return self._get(
            "/api/test/endpoint-6",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimpleResponse,
        )

    def test_endpoint_7(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SimpleResponse:
        """Test Endpoint 7"""
        return self._get(
            "/api/test/endpoint-7",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimpleResponse,
        )

    def test_endpoint_8(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SimpleResponse:
        """Test Endpoint 8"""
        return self._get(
            "/api/test/endpoint-8",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimpleResponse,
        )

    def test_endpoint_9(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SimpleResponse:
        """Test Endpoint 9"""
        return self._get(
            "/api/test/endpoint-9",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimpleResponse,
        )


class AsyncTestResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTestResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/arbitrationcity/arbi-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTestResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTestResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/arbitrationcity/arbi-python#with_streaming_response
        """
        return AsyncTestResourceWithStreamingResponse(self)

    async def test_endpoint_1(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SimpleResponse:
        """Test Endpoint 1"""
        return await self._get(
            "/api/test/endpoint-1",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimpleResponse,
        )

    async def test_endpoint_10(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SimpleResponse:
        """Test Endpoint 10"""
        return await self._get(
            "/api/test/endpoint-10",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimpleResponse,
        )

    async def test_endpoint_11(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SimpleResponse:
        """Test Endpoint 11"""
        return await self._get(
            "/api/test/endpoint-11",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimpleResponse,
        )

    async def test_endpoint_12(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SimpleResponse:
        """Test Endpoint 12"""
        return await self._get(
            "/api/test/endpoint-12",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimpleResponse,
        )

    async def test_endpoint_13(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SimpleResponse:
        """Test Endpoint 13"""
        return await self._get(
            "/api/test/endpoint-13",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimpleResponse,
        )

    async def test_endpoint_14(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SimpleResponse:
        """Test Endpoint 14"""
        return await self._get(
            "/api/test/endpoint-14",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimpleResponse,
        )

    async def test_endpoint_15(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SimpleResponse:
        """Test Endpoint 15"""
        return await self._get(
            "/api/test/endpoint-15",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimpleResponse,
        )

    async def test_endpoint_16(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SimpleResponse:
        """Test Endpoint 16"""
        return await self._get(
            "/api/test/endpoint-16",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimpleResponse,
        )

    async def test_endpoint_17(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SimpleResponse:
        """Test Endpoint 17"""
        return await self._get(
            "/api/test/endpoint-17",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimpleResponse,
        )

    async def test_endpoint_18(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SimpleResponse:
        """Test Endpoint 18"""
        return await self._get(
            "/api/test/endpoint-18",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimpleResponse,
        )

    async def test_endpoint_19(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SimpleResponse:
        """Test Endpoint 19"""
        return await self._get(
            "/api/test/endpoint-19",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimpleResponse,
        )

    async def test_endpoint_2(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SimpleResponse:
        """Test Endpoint 2"""
        return await self._get(
            "/api/test/endpoint-2",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimpleResponse,
        )

    async def test_endpoint_20(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SimpleResponse:
        """Test Endpoint 20"""
        return await self._get(
            "/api/test/endpoint-20",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimpleResponse,
        )

    async def test_endpoint_21(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SimpleResponse:
        """Test Endpoint 21"""
        return await self._get(
            "/api/test/endpoint-21",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimpleResponse,
        )

    async def test_endpoint_22(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SimpleResponse:
        """Test Endpoint 22"""
        return await self._get(
            "/api/test/endpoint-22",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimpleResponse,
        )

    async def test_endpoint_23(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SimpleResponse:
        """Test Endpoint 23"""
        return await self._get(
            "/api/test/endpoint-23",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimpleResponse,
        )

    async def test_endpoint_24(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SimpleResponse:
        """Test Endpoint 24"""
        return await self._get(
            "/api/test/endpoint-24",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimpleResponse,
        )

    async def test_endpoint_25(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SimpleResponse:
        """Test Endpoint 25"""
        return await self._get(
            "/api/test/endpoint-25",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimpleResponse,
        )

    async def test_endpoint_26(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SimpleResponse:
        """Test Endpoint 26"""
        return await self._get(
            "/api/test/endpoint-26",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimpleResponse,
        )

    async def test_endpoint_27(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SimpleResponse:
        """Test Endpoint 27"""
        return await self._get(
            "/api/test/endpoint-27",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimpleResponse,
        )

    async def test_endpoint_28(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SimpleResponse:
        """Test Endpoint 28"""
        return await self._get(
            "/api/test/endpoint-28",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimpleResponse,
        )

    async def test_endpoint_29(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SimpleResponse:
        """Test Endpoint 29"""
        return await self._get(
            "/api/test/endpoint-29",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimpleResponse,
        )

    async def test_endpoint_3(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SimpleResponse:
        """Test Endpoint 3"""
        return await self._get(
            "/api/test/endpoint-3",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimpleResponse,
        )

    async def test_endpoint_30(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SimpleResponse:
        """Test Endpoint 30"""
        return await self._get(
            "/api/test/endpoint-30",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimpleResponse,
        )

    async def test_endpoint_4(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SimpleResponse:
        """Test Endpoint 4"""
        return await self._get(
            "/api/test/endpoint-4",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimpleResponse,
        )

    async def test_endpoint_5(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SimpleResponse:
        """Test Endpoint 5"""
        return await self._get(
            "/api/test/endpoint-5",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimpleResponse,
        )

    async def test_endpoint_6(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SimpleResponse:
        """Test Endpoint 6"""
        return await self._get(
            "/api/test/endpoint-6",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimpleResponse,
        )

    async def test_endpoint_7(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SimpleResponse:
        """Test Endpoint 7"""
        return await self._get(
            "/api/test/endpoint-7",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimpleResponse,
        )

    async def test_endpoint_8(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SimpleResponse:
        """Test Endpoint 8"""
        return await self._get(
            "/api/test/endpoint-8",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimpleResponse,
        )

    async def test_endpoint_9(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SimpleResponse:
        """Test Endpoint 9"""
        return await self._get(
            "/api/test/endpoint-9",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimpleResponse,
        )


class TestResourceWithRawResponse:
    __test__ = False

    def __init__(self, test: TestResource) -> None:
        self._test = test

        self.test_endpoint_1 = to_raw_response_wrapper(
            test.test_endpoint_1,
        )
        self.test_endpoint_10 = to_raw_response_wrapper(
            test.test_endpoint_10,
        )
        self.test_endpoint_11 = to_raw_response_wrapper(
            test.test_endpoint_11,
        )
        self.test_endpoint_12 = to_raw_response_wrapper(
            test.test_endpoint_12,
        )
        self.test_endpoint_13 = to_raw_response_wrapper(
            test.test_endpoint_13,
        )
        self.test_endpoint_14 = to_raw_response_wrapper(
            test.test_endpoint_14,
        )
        self.test_endpoint_15 = to_raw_response_wrapper(
            test.test_endpoint_15,
        )
        self.test_endpoint_16 = to_raw_response_wrapper(
            test.test_endpoint_16,
        )
        self.test_endpoint_17 = to_raw_response_wrapper(
            test.test_endpoint_17,
        )
        self.test_endpoint_18 = to_raw_response_wrapper(
            test.test_endpoint_18,
        )
        self.test_endpoint_19 = to_raw_response_wrapper(
            test.test_endpoint_19,
        )
        self.test_endpoint_2 = to_raw_response_wrapper(
            test.test_endpoint_2,
        )
        self.test_endpoint_20 = to_raw_response_wrapper(
            test.test_endpoint_20,
        )
        self.test_endpoint_21 = to_raw_response_wrapper(
            test.test_endpoint_21,
        )
        self.test_endpoint_22 = to_raw_response_wrapper(
            test.test_endpoint_22,
        )
        self.test_endpoint_23 = to_raw_response_wrapper(
            test.test_endpoint_23,
        )
        self.test_endpoint_24 = to_raw_response_wrapper(
            test.test_endpoint_24,
        )
        self.test_endpoint_25 = to_raw_response_wrapper(
            test.test_endpoint_25,
        )
        self.test_endpoint_26 = to_raw_response_wrapper(
            test.test_endpoint_26,
        )
        self.test_endpoint_27 = to_raw_response_wrapper(
            test.test_endpoint_27,
        )
        self.test_endpoint_28 = to_raw_response_wrapper(
            test.test_endpoint_28,
        )
        self.test_endpoint_29 = to_raw_response_wrapper(
            test.test_endpoint_29,
        )
        self.test_endpoint_3 = to_raw_response_wrapper(
            test.test_endpoint_3,
        )
        self.test_endpoint_30 = to_raw_response_wrapper(
            test.test_endpoint_30,
        )
        self.test_endpoint_4 = to_raw_response_wrapper(
            test.test_endpoint_4,
        )
        self.test_endpoint_5 = to_raw_response_wrapper(
            test.test_endpoint_5,
        )
        self.test_endpoint_6 = to_raw_response_wrapper(
            test.test_endpoint_6,
        )
        self.test_endpoint_7 = to_raw_response_wrapper(
            test.test_endpoint_7,
        )
        self.test_endpoint_8 = to_raw_response_wrapper(
            test.test_endpoint_8,
        )
        self.test_endpoint_9 = to_raw_response_wrapper(
            test.test_endpoint_9,
        )


class AsyncTestResourceWithRawResponse:
    def __init__(self, test: AsyncTestResource) -> None:
        self._test = test

        self.test_endpoint_1 = async_to_raw_response_wrapper(
            test.test_endpoint_1,
        )
        self.test_endpoint_10 = async_to_raw_response_wrapper(
            test.test_endpoint_10,
        )
        self.test_endpoint_11 = async_to_raw_response_wrapper(
            test.test_endpoint_11,
        )
        self.test_endpoint_12 = async_to_raw_response_wrapper(
            test.test_endpoint_12,
        )
        self.test_endpoint_13 = async_to_raw_response_wrapper(
            test.test_endpoint_13,
        )
        self.test_endpoint_14 = async_to_raw_response_wrapper(
            test.test_endpoint_14,
        )
        self.test_endpoint_15 = async_to_raw_response_wrapper(
            test.test_endpoint_15,
        )
        self.test_endpoint_16 = async_to_raw_response_wrapper(
            test.test_endpoint_16,
        )
        self.test_endpoint_17 = async_to_raw_response_wrapper(
            test.test_endpoint_17,
        )
        self.test_endpoint_18 = async_to_raw_response_wrapper(
            test.test_endpoint_18,
        )
        self.test_endpoint_19 = async_to_raw_response_wrapper(
            test.test_endpoint_19,
        )
        self.test_endpoint_2 = async_to_raw_response_wrapper(
            test.test_endpoint_2,
        )
        self.test_endpoint_20 = async_to_raw_response_wrapper(
            test.test_endpoint_20,
        )
        self.test_endpoint_21 = async_to_raw_response_wrapper(
            test.test_endpoint_21,
        )
        self.test_endpoint_22 = async_to_raw_response_wrapper(
            test.test_endpoint_22,
        )
        self.test_endpoint_23 = async_to_raw_response_wrapper(
            test.test_endpoint_23,
        )
        self.test_endpoint_24 = async_to_raw_response_wrapper(
            test.test_endpoint_24,
        )
        self.test_endpoint_25 = async_to_raw_response_wrapper(
            test.test_endpoint_25,
        )
        self.test_endpoint_26 = async_to_raw_response_wrapper(
            test.test_endpoint_26,
        )
        self.test_endpoint_27 = async_to_raw_response_wrapper(
            test.test_endpoint_27,
        )
        self.test_endpoint_28 = async_to_raw_response_wrapper(
            test.test_endpoint_28,
        )
        self.test_endpoint_29 = async_to_raw_response_wrapper(
            test.test_endpoint_29,
        )
        self.test_endpoint_3 = async_to_raw_response_wrapper(
            test.test_endpoint_3,
        )
        self.test_endpoint_30 = async_to_raw_response_wrapper(
            test.test_endpoint_30,
        )
        self.test_endpoint_4 = async_to_raw_response_wrapper(
            test.test_endpoint_4,
        )
        self.test_endpoint_5 = async_to_raw_response_wrapper(
            test.test_endpoint_5,
        )
        self.test_endpoint_6 = async_to_raw_response_wrapper(
            test.test_endpoint_6,
        )
        self.test_endpoint_7 = async_to_raw_response_wrapper(
            test.test_endpoint_7,
        )
        self.test_endpoint_8 = async_to_raw_response_wrapper(
            test.test_endpoint_8,
        )
        self.test_endpoint_9 = async_to_raw_response_wrapper(
            test.test_endpoint_9,
        )


class TestResourceWithStreamingResponse:
    __test__ = False

    def __init__(self, test: TestResource) -> None:
        self._test = test

        self.test_endpoint_1 = to_streamed_response_wrapper(
            test.test_endpoint_1,
        )
        self.test_endpoint_10 = to_streamed_response_wrapper(
            test.test_endpoint_10,
        )
        self.test_endpoint_11 = to_streamed_response_wrapper(
            test.test_endpoint_11,
        )
        self.test_endpoint_12 = to_streamed_response_wrapper(
            test.test_endpoint_12,
        )
        self.test_endpoint_13 = to_streamed_response_wrapper(
            test.test_endpoint_13,
        )
        self.test_endpoint_14 = to_streamed_response_wrapper(
            test.test_endpoint_14,
        )
        self.test_endpoint_15 = to_streamed_response_wrapper(
            test.test_endpoint_15,
        )
        self.test_endpoint_16 = to_streamed_response_wrapper(
            test.test_endpoint_16,
        )
        self.test_endpoint_17 = to_streamed_response_wrapper(
            test.test_endpoint_17,
        )
        self.test_endpoint_18 = to_streamed_response_wrapper(
            test.test_endpoint_18,
        )
        self.test_endpoint_19 = to_streamed_response_wrapper(
            test.test_endpoint_19,
        )
        self.test_endpoint_2 = to_streamed_response_wrapper(
            test.test_endpoint_2,
        )
        self.test_endpoint_20 = to_streamed_response_wrapper(
            test.test_endpoint_20,
        )
        self.test_endpoint_21 = to_streamed_response_wrapper(
            test.test_endpoint_21,
        )
        self.test_endpoint_22 = to_streamed_response_wrapper(
            test.test_endpoint_22,
        )
        self.test_endpoint_23 = to_streamed_response_wrapper(
            test.test_endpoint_23,
        )
        self.test_endpoint_24 = to_streamed_response_wrapper(
            test.test_endpoint_24,
        )
        self.test_endpoint_25 = to_streamed_response_wrapper(
            test.test_endpoint_25,
        )
        self.test_endpoint_26 = to_streamed_response_wrapper(
            test.test_endpoint_26,
        )
        self.test_endpoint_27 = to_streamed_response_wrapper(
            test.test_endpoint_27,
        )
        self.test_endpoint_28 = to_streamed_response_wrapper(
            test.test_endpoint_28,
        )
        self.test_endpoint_29 = to_streamed_response_wrapper(
            test.test_endpoint_29,
        )
        self.test_endpoint_3 = to_streamed_response_wrapper(
            test.test_endpoint_3,
        )
        self.test_endpoint_30 = to_streamed_response_wrapper(
            test.test_endpoint_30,
        )
        self.test_endpoint_4 = to_streamed_response_wrapper(
            test.test_endpoint_4,
        )
        self.test_endpoint_5 = to_streamed_response_wrapper(
            test.test_endpoint_5,
        )
        self.test_endpoint_6 = to_streamed_response_wrapper(
            test.test_endpoint_6,
        )
        self.test_endpoint_7 = to_streamed_response_wrapper(
            test.test_endpoint_7,
        )
        self.test_endpoint_8 = to_streamed_response_wrapper(
            test.test_endpoint_8,
        )
        self.test_endpoint_9 = to_streamed_response_wrapper(
            test.test_endpoint_9,
        )


class AsyncTestResourceWithStreamingResponse:
    def __init__(self, test: AsyncTestResource) -> None:
        self._test = test

        self.test_endpoint_1 = async_to_streamed_response_wrapper(
            test.test_endpoint_1,
        )
        self.test_endpoint_10 = async_to_streamed_response_wrapper(
            test.test_endpoint_10,
        )
        self.test_endpoint_11 = async_to_streamed_response_wrapper(
            test.test_endpoint_11,
        )
        self.test_endpoint_12 = async_to_streamed_response_wrapper(
            test.test_endpoint_12,
        )
        self.test_endpoint_13 = async_to_streamed_response_wrapper(
            test.test_endpoint_13,
        )
        self.test_endpoint_14 = async_to_streamed_response_wrapper(
            test.test_endpoint_14,
        )
        self.test_endpoint_15 = async_to_streamed_response_wrapper(
            test.test_endpoint_15,
        )
        self.test_endpoint_16 = async_to_streamed_response_wrapper(
            test.test_endpoint_16,
        )
        self.test_endpoint_17 = async_to_streamed_response_wrapper(
            test.test_endpoint_17,
        )
        self.test_endpoint_18 = async_to_streamed_response_wrapper(
            test.test_endpoint_18,
        )
        self.test_endpoint_19 = async_to_streamed_response_wrapper(
            test.test_endpoint_19,
        )
        self.test_endpoint_2 = async_to_streamed_response_wrapper(
            test.test_endpoint_2,
        )
        self.test_endpoint_20 = async_to_streamed_response_wrapper(
            test.test_endpoint_20,
        )
        self.test_endpoint_21 = async_to_streamed_response_wrapper(
            test.test_endpoint_21,
        )
        self.test_endpoint_22 = async_to_streamed_response_wrapper(
            test.test_endpoint_22,
        )
        self.test_endpoint_23 = async_to_streamed_response_wrapper(
            test.test_endpoint_23,
        )
        self.test_endpoint_24 = async_to_streamed_response_wrapper(
            test.test_endpoint_24,
        )
        self.test_endpoint_25 = async_to_streamed_response_wrapper(
            test.test_endpoint_25,
        )
        self.test_endpoint_26 = async_to_streamed_response_wrapper(
            test.test_endpoint_26,
        )
        self.test_endpoint_27 = async_to_streamed_response_wrapper(
            test.test_endpoint_27,
        )
        self.test_endpoint_28 = async_to_streamed_response_wrapper(
            test.test_endpoint_28,
        )
        self.test_endpoint_29 = async_to_streamed_response_wrapper(
            test.test_endpoint_29,
        )
        self.test_endpoint_3 = async_to_streamed_response_wrapper(
            test.test_endpoint_3,
        )
        self.test_endpoint_30 = async_to_streamed_response_wrapper(
            test.test_endpoint_30,
        )
        self.test_endpoint_4 = async_to_streamed_response_wrapper(
            test.test_endpoint_4,
        )
        self.test_endpoint_5 = async_to_streamed_response_wrapper(
            test.test_endpoint_5,
        )
        self.test_endpoint_6 = async_to_streamed_response_wrapper(
            test.test_endpoint_6,
        )
        self.test_endpoint_7 = async_to_streamed_response_wrapper(
            test.test_endpoint_7,
        )
        self.test_endpoint_8 = async_to_streamed_response_wrapper(
            test.test_endpoint_8,
        )
        self.test_endpoint_9 = async_to_streamed_response_wrapper(
            test.test_endpoint_9,
        )
