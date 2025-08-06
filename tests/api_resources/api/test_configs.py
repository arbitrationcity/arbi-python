# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from arbi import Arbi, AsyncArbi
from tests.utils import assert_matches_type
from arbi.types.api import ConfigRetrieveSchemaResponse, ConfigRetrieveVersionsResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestConfigs:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve_schema(self, client: Arbi) -> None:
        config = client.api.configs.retrieve_schema()
        assert_matches_type(ConfigRetrieveSchemaResponse, config, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve_schema(self, client: Arbi) -> None:
        response = client.api.configs.with_raw_response.retrieve_schema()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config = response.parse()
        assert_matches_type(ConfigRetrieveSchemaResponse, config, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve_schema(self, client: Arbi) -> None:
        with client.api.configs.with_streaming_response.retrieve_schema() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config = response.parse()
            assert_matches_type(ConfigRetrieveSchemaResponse, config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve_versions(self, client: Arbi) -> None:
        config = client.api.configs.retrieve_versions()
        assert_matches_type(ConfigRetrieveVersionsResponse, config, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve_versions(self, client: Arbi) -> None:
        response = client.api.configs.with_raw_response.retrieve_versions()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config = response.parse()
        assert_matches_type(ConfigRetrieveVersionsResponse, config, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve_versions(self, client: Arbi) -> None:
        with client.api.configs.with_streaming_response.retrieve_versions() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config = response.parse()
            assert_matches_type(ConfigRetrieveVersionsResponse, config, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncConfigs:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve_schema(self, async_client: AsyncArbi) -> None:
        config = await async_client.api.configs.retrieve_schema()
        assert_matches_type(ConfigRetrieveSchemaResponse, config, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve_schema(self, async_client: AsyncArbi) -> None:
        response = await async_client.api.configs.with_raw_response.retrieve_schema()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config = await response.parse()
        assert_matches_type(ConfigRetrieveSchemaResponse, config, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve_schema(self, async_client: AsyncArbi) -> None:
        async with async_client.api.configs.with_streaming_response.retrieve_schema() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config = await response.parse()
            assert_matches_type(ConfigRetrieveSchemaResponse, config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve_versions(self, async_client: AsyncArbi) -> None:
        config = await async_client.api.configs.retrieve_versions()
        assert_matches_type(ConfigRetrieveVersionsResponse, config, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve_versions(self, async_client: AsyncArbi) -> None:
        response = await async_client.api.configs.with_raw_response.retrieve_versions()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config = await response.parse()
        assert_matches_type(ConfigRetrieveVersionsResponse, config, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve_versions(self, async_client: AsyncArbi) -> None:
        async with async_client.api.configs.with_streaming_response.retrieve_versions() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config = await response.parse()
            assert_matches_type(ConfigRetrieveVersionsResponse, config, path=["response"])

        assert cast(Any, response.is_closed) is True
