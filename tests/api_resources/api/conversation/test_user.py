# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from arbi import Arbi, AsyncArbi
from tests.utils import assert_matches_type
from arbi.types.api.conversation import (
    UserCreateResponse,
    UserDeleteAllResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestUser:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Arbi) -> None:
        user = client.api.conversation.user.create(
            conversation_ext_id="con",
            user_ext_id="usr-bFXA5r3A",
        )
        assert_matches_type(UserCreateResponse, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Arbi) -> None:
        response = client.api.conversation.user.with_raw_response.create(
            conversation_ext_id="con",
            user_ext_id="usr-bFXA5r3A",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(UserCreateResponse, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Arbi) -> None:
        with client.api.conversation.user.with_streaming_response.create(
            conversation_ext_id="con",
            user_ext_id="usr-bFXA5r3A",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(UserCreateResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_create(self, client: Arbi) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `conversation_ext_id` but received ''"):
            client.api.conversation.user.with_raw_response.create(
                conversation_ext_id="",
                user_ext_id="usr-bFXA5r3A",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete_all(self, client: Arbi) -> None:
        user = client.api.conversation.user.delete_all(
            conversation_ext_id="con",
            user_ext_id="usr-bFXA5r3A",
        )
        assert_matches_type(UserDeleteAllResponse, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete_all(self, client: Arbi) -> None:
        response = client.api.conversation.user.with_raw_response.delete_all(
            conversation_ext_id="con",
            user_ext_id="usr-bFXA5r3A",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(UserDeleteAllResponse, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete_all(self, client: Arbi) -> None:
        with client.api.conversation.user.with_streaming_response.delete_all(
            conversation_ext_id="con",
            user_ext_id="usr-bFXA5r3A",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(UserDeleteAllResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete_all(self, client: Arbi) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `conversation_ext_id` but received ''"):
            client.api.conversation.user.with_raw_response.delete_all(
                conversation_ext_id="",
                user_ext_id="usr-bFXA5r3A",
            )


class TestAsyncUser:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncArbi) -> None:
        user = await async_client.api.conversation.user.create(
            conversation_ext_id="con",
            user_ext_id="usr-bFXA5r3A",
        )
        assert_matches_type(UserCreateResponse, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncArbi) -> None:
        response = await async_client.api.conversation.user.with_raw_response.create(
            conversation_ext_id="con",
            user_ext_id="usr-bFXA5r3A",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(UserCreateResponse, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncArbi) -> None:
        async with async_client.api.conversation.user.with_streaming_response.create(
            conversation_ext_id="con",
            user_ext_id="usr-bFXA5r3A",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(UserCreateResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncArbi) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `conversation_ext_id` but received ''"):
            await async_client.api.conversation.user.with_raw_response.create(
                conversation_ext_id="",
                user_ext_id="usr-bFXA5r3A",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete_all(self, async_client: AsyncArbi) -> None:
        user = await async_client.api.conversation.user.delete_all(
            conversation_ext_id="con",
            user_ext_id="usr-bFXA5r3A",
        )
        assert_matches_type(UserDeleteAllResponse, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete_all(self, async_client: AsyncArbi) -> None:
        response = await async_client.api.conversation.user.with_raw_response.delete_all(
            conversation_ext_id="con",
            user_ext_id="usr-bFXA5r3A",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(UserDeleteAllResponse, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete_all(self, async_client: AsyncArbi) -> None:
        async with async_client.api.conversation.user.with_streaming_response.delete_all(
            conversation_ext_id="con",
            user_ext_id="usr-bFXA5r3A",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(UserDeleteAllResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete_all(self, async_client: AsyncArbi) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `conversation_ext_id` but received ''"):
            await async_client.api.conversation.user.with_raw_response.delete_all(
                conversation_ext_id="",
                user_ext_id="usr-bFXA5r3A",
            )
