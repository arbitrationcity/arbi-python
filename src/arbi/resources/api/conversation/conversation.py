# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .user import (
    UserResource,
    AsyncUserResource,
    UserResourceWithRawResponse,
    AsyncUserResourceWithRawResponse,
    UserResourceWithStreamingResponse,
    AsyncUserResourceWithStreamingResponse,
)
from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.api.conversation_share_response import ConversationShareResponse
from ....types.api.conversation_delete_response import ConversationDeleteResponse
from ....types.api.conversation_retrieve_threads_response import ConversationRetrieveThreadsResponse

__all__ = ["ConversationResource", "AsyncConversationResource"]


class ConversationResource(SyncAPIResource):
    @cached_property
    def user(self) -> UserResource:
        return UserResource(self._client)

    @cached_property
    def with_raw_response(self) -> ConversationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/arbi-python#accessing-raw-response-data-eg-headers
        """
        return ConversationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ConversationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/arbi-python#with_streaming_response
        """
        return ConversationResourceWithStreamingResponse(self)

    def delete(
        self,
        message_ext_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConversationDeleteResponse:
        """
        Delete a message along with all descendants.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not message_ext_id:
            raise ValueError(f"Expected a non-empty value for `message_ext_id` but received {message_ext_id!r}")
        return self._delete(
            f"/api/conversation/message/{message_ext_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConversationDeleteResponse,
        )

    def retrieve_threads(
        self,
        conversation_ext_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConversationRetrieveThreadsResponse:
        """
        Retrieve all conversation threads (leaf messages and their histories) for a
        given conversation external ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not conversation_ext_id:
            raise ValueError(
                f"Expected a non-empty value for `conversation_ext_id` but received {conversation_ext_id!r}"
            )
        return self._get(
            f"/api/conversation/{conversation_ext_id}/threads",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConversationRetrieveThreadsResponse,
        )

    def share(
        self,
        conversation_ext_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConversationShareResponse:
        """
        Share all messages in a conversation by setting their shared flag to true.

        Only the conversation creator can share a conversation.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not conversation_ext_id:
            raise ValueError(
                f"Expected a non-empty value for `conversation_ext_id` but received {conversation_ext_id!r}"
            )
        return self._post(
            f"/api/conversation/{conversation_ext_id}/share",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConversationShareResponse,
        )


class AsyncConversationResource(AsyncAPIResource):
    @cached_property
    def user(self) -> AsyncUserResource:
        return AsyncUserResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncConversationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/arbi-python#accessing-raw-response-data-eg-headers
        """
        return AsyncConversationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncConversationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/arbi-python#with_streaming_response
        """
        return AsyncConversationResourceWithStreamingResponse(self)

    async def delete(
        self,
        message_ext_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConversationDeleteResponse:
        """
        Delete a message along with all descendants.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not message_ext_id:
            raise ValueError(f"Expected a non-empty value for `message_ext_id` but received {message_ext_id!r}")
        return await self._delete(
            f"/api/conversation/message/{message_ext_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConversationDeleteResponse,
        )

    async def retrieve_threads(
        self,
        conversation_ext_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConversationRetrieveThreadsResponse:
        """
        Retrieve all conversation threads (leaf messages and their histories) for a
        given conversation external ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not conversation_ext_id:
            raise ValueError(
                f"Expected a non-empty value for `conversation_ext_id` but received {conversation_ext_id!r}"
            )
        return await self._get(
            f"/api/conversation/{conversation_ext_id}/threads",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConversationRetrieveThreadsResponse,
        )

    async def share(
        self,
        conversation_ext_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConversationShareResponse:
        """
        Share all messages in a conversation by setting their shared flag to true.

        Only the conversation creator can share a conversation.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not conversation_ext_id:
            raise ValueError(
                f"Expected a non-empty value for `conversation_ext_id` but received {conversation_ext_id!r}"
            )
        return await self._post(
            f"/api/conversation/{conversation_ext_id}/share",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConversationShareResponse,
        )


class ConversationResourceWithRawResponse:
    def __init__(self, conversation: ConversationResource) -> None:
        self._conversation = conversation

        self.delete = to_raw_response_wrapper(
            conversation.delete,
        )
        self.retrieve_threads = to_raw_response_wrapper(
            conversation.retrieve_threads,
        )
        self.share = to_raw_response_wrapper(
            conversation.share,
        )

    @cached_property
    def user(self) -> UserResourceWithRawResponse:
        return UserResourceWithRawResponse(self._conversation.user)


class AsyncConversationResourceWithRawResponse:
    def __init__(self, conversation: AsyncConversationResource) -> None:
        self._conversation = conversation

        self.delete = async_to_raw_response_wrapper(
            conversation.delete,
        )
        self.retrieve_threads = async_to_raw_response_wrapper(
            conversation.retrieve_threads,
        )
        self.share = async_to_raw_response_wrapper(
            conversation.share,
        )

    @cached_property
    def user(self) -> AsyncUserResourceWithRawResponse:
        return AsyncUserResourceWithRawResponse(self._conversation.user)


class ConversationResourceWithStreamingResponse:
    def __init__(self, conversation: ConversationResource) -> None:
        self._conversation = conversation

        self.delete = to_streamed_response_wrapper(
            conversation.delete,
        )
        self.retrieve_threads = to_streamed_response_wrapper(
            conversation.retrieve_threads,
        )
        self.share = to_streamed_response_wrapper(
            conversation.share,
        )

    @cached_property
    def user(self) -> UserResourceWithStreamingResponse:
        return UserResourceWithStreamingResponse(self._conversation.user)


class AsyncConversationResourceWithStreamingResponse:
    def __init__(self, conversation: AsyncConversationResource) -> None:
        self._conversation = conversation

        self.delete = async_to_streamed_response_wrapper(
            conversation.delete,
        )
        self.retrieve_threads = async_to_streamed_response_wrapper(
            conversation.retrieve_threads,
        )
        self.share = async_to_streamed_response_wrapper(
            conversation.share,
        )

    @cached_property
    def user(self) -> AsyncUserResourceWithStreamingResponse:
        return AsyncUserResourceWithStreamingResponse(self._conversation.user)
