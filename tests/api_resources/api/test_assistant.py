# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from arbi import Arbi, AsyncArbi
from tests.utils import assert_matches_type
from arbi.types.api import (
    AssistantCreateCitationsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAssistant:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve(self, client: Arbi) -> None:
        assistant = client.api.assistant.retrieve(
            content="content",
            workspace_ext_id="workspace_ext_id",
        )
        assert_matches_type(object, assistant, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve_with_all_params(self, client: Arbi) -> None:
        assistant = client.api.assistant.retrieve(
            content="content",
            workspace_ext_id="workspace_ext_id",
            model="model",
            parent_message_ext_id="parent_message_ext_id",
            system_message="system_message",
            tools={
                "foo": {
                    "description": "description",
                    "name": "name",
                    "tool_args": {"foo": "bar"},
                    "tool_responses": {"foo": "bar"},
                }
            },
        )
        assert_matches_type(object, assistant, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve(self, client: Arbi) -> None:
        response = client.api.assistant.with_raw_response.retrieve(
            content="content",
            workspace_ext_id="workspace_ext_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        assistant = response.parse()
        assert_matches_type(object, assistant, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve(self, client: Arbi) -> None:
        with client.api.assistant.with_streaming_response.retrieve(
            content="content",
            workspace_ext_id="workspace_ext_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            assistant = response.parse()
            assert_matches_type(object, assistant, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_create_citations(self, client: Arbi) -> None:
        assistant = client.api.assistant.create_citations(
            message_id="message_id",
        )
        assert_matches_type(AssistantCreateCitationsResponse, assistant, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create_citations(self, client: Arbi) -> None:
        response = client.api.assistant.with_raw_response.create_citations(
            message_id="message_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        assistant = response.parse()
        assert_matches_type(AssistantCreateCitationsResponse, assistant, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create_citations(self, client: Arbi) -> None:
        with client.api.assistant.with_streaming_response.create_citations(
            message_id="message_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            assistant = response.parse()
            assert_matches_type(AssistantCreateCitationsResponse, assistant, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_query(self, client: Arbi) -> None:
        assistant = client.api.assistant.query(
            content="content",
            workspace_ext_id="workspace_ext_id",
        )
        assert_matches_type(object, assistant, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_query_with_all_params(self, client: Arbi) -> None:
        assistant = client.api.assistant.query(
            content="content",
            workspace_ext_id="workspace_ext_id",
            model="model",
            parent_message_ext_id="parent_message_ext_id",
            system_message="system_message",
            tools={
                "foo": {
                    "description": "description",
                    "name": "name",
                    "tool_args": {"foo": "bar"},
                    "tool_responses": {"foo": "bar"},
                }
            },
        )
        assert_matches_type(object, assistant, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_query(self, client: Arbi) -> None:
        response = client.api.assistant.with_raw_response.query(
            content="content",
            workspace_ext_id="workspace_ext_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        assistant = response.parse()
        assert_matches_type(object, assistant, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_query(self, client: Arbi) -> None:
        with client.api.assistant.with_streaming_response.query(
            content="content",
            workspace_ext_id="workspace_ext_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            assistant = response.parse()
            assert_matches_type(object, assistant, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAssistant:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncArbi) -> None:
        assistant = await async_client.api.assistant.retrieve(
            content="content",
            workspace_ext_id="workspace_ext_id",
        )
        assert_matches_type(object, assistant, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncArbi) -> None:
        assistant = await async_client.api.assistant.retrieve(
            content="content",
            workspace_ext_id="workspace_ext_id",
            model="model",
            parent_message_ext_id="parent_message_ext_id",
            system_message="system_message",
            tools={
                "foo": {
                    "description": "description",
                    "name": "name",
                    "tool_args": {"foo": "bar"},
                    "tool_responses": {"foo": "bar"},
                }
            },
        )
        assert_matches_type(object, assistant, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncArbi) -> None:
        response = await async_client.api.assistant.with_raw_response.retrieve(
            content="content",
            workspace_ext_id="workspace_ext_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        assistant = await response.parse()
        assert_matches_type(object, assistant, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncArbi) -> None:
        async with async_client.api.assistant.with_streaming_response.retrieve(
            content="content",
            workspace_ext_id="workspace_ext_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            assistant = await response.parse()
            assert_matches_type(object, assistant, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_citations(self, async_client: AsyncArbi) -> None:
        assistant = await async_client.api.assistant.create_citations(
            message_id="message_id",
        )
        assert_matches_type(AssistantCreateCitationsResponse, assistant, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create_citations(self, async_client: AsyncArbi) -> None:
        response = await async_client.api.assistant.with_raw_response.create_citations(
            message_id="message_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        assistant = await response.parse()
        assert_matches_type(AssistantCreateCitationsResponse, assistant, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create_citations(self, async_client: AsyncArbi) -> None:
        async with async_client.api.assistant.with_streaming_response.create_citations(
            message_id="message_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            assistant = await response.parse()
            assert_matches_type(AssistantCreateCitationsResponse, assistant, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_query(self, async_client: AsyncArbi) -> None:
        assistant = await async_client.api.assistant.query(
            content="content",
            workspace_ext_id="workspace_ext_id",
        )
        assert_matches_type(object, assistant, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_query_with_all_params(self, async_client: AsyncArbi) -> None:
        assistant = await async_client.api.assistant.query(
            content="content",
            workspace_ext_id="workspace_ext_id",
            model="model",
            parent_message_ext_id="parent_message_ext_id",
            system_message="system_message",
            tools={
                "foo": {
                    "description": "description",
                    "name": "name",
                    "tool_args": {"foo": "bar"},
                    "tool_responses": {"foo": "bar"},
                }
            },
        )
        assert_matches_type(object, assistant, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_query(self, async_client: AsyncArbi) -> None:
        response = await async_client.api.assistant.with_raw_response.query(
            content="content",
            workspace_ext_id="workspace_ext_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        assistant = await response.parse()
        assert_matches_type(object, assistant, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_query(self, async_client: AsyncArbi) -> None:
        async with async_client.api.assistant.with_streaming_response.query(
            content="content",
            workspace_ext_id="workspace_ext_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            assistant = await response.parse()
            assert_matches_type(object, assistant, path=["response"])

        assert cast(Any, response.is_closed) is True
