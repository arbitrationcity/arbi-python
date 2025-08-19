# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from arbi import Arbi, AsyncArbi
from tests.utils import assert_matches_type
from arbi.types.api import (
    ConfigUpdateResponse,
    ConfigRetrieveVersionsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestConfigs:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: Arbi) -> None:
        config = client.api.configs.update()
        assert_matches_type(ConfigUpdateResponse, config, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Arbi) -> None:
        config = client.api.configs.update(
            chunker={},
            document_date_extractor_llm={
                "api_type": "local",
                "max_char_size_to_answer": 0,
                "max_tokens": 0,
                "model_name": "MODEL_NAME",
                "system_instruction": "SYSTEM_INSTRUCTION",
                "temperature": 0,
            },
            embedder={
                "api_type": "local",
                "model_name": "MODEL_NAME",
            },
            model_citation={
                "max_numb_citations": 0,
                "min_char_size_to_answer": 0,
                "sim_model_name": "SIM_MODEL_NAME",
                "sim_threashold": 0,
            },
            parent_message_ext_id="parent_message_ext_id",
            parser={},
            query_llm={
                "api_type": "local",
                "max_char_size_to_answer": 0,
                "max_tokens": 0,
                "model_name": "MODEL_NAME",
                "system_instruction": "SYSTEM_INSTRUCTION",
                "temperature": 0,
            },
            reranker={
                "api_type": "local",
                "max_numb_of_chunks": 1,
                "model_name": "MODEL_NAME",
            },
            retriever={
                "group_size": 1000,
                "max_distinct_documents": 100,
                "max_total_chunks_to_retrieve": 100,
                "min_retrieval_sim_score": 0,
            },
            title="title",
            title_llm={
                "api_type": "local",
                "max_char_size_to_answer": 0,
                "max_tokens": 0,
                "model_name": "MODEL_NAME",
                "system_instruction": "SYSTEM_INSTRUCTION",
                "temperature": 0,
            },
        )
        assert_matches_type(ConfigUpdateResponse, config, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Arbi) -> None:
        response = client.api.configs.with_raw_response.update()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config = response.parse()
        assert_matches_type(ConfigUpdateResponse, config, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Arbi) -> None:
        with client.api.configs.with_streaming_response.update() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config = response.parse()
            assert_matches_type(ConfigUpdateResponse, config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_schema(self, client: Arbi) -> None:
        config = client.api.configs.retrieve_schema()
        assert_matches_type(object, config, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve_schema(self, client: Arbi) -> None:
        response = client.api.configs.with_raw_response.retrieve_schema()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config = response.parse()
        assert_matches_type(object, config, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_schema(self, client: Arbi) -> None:
        with client.api.configs.with_streaming_response.retrieve_schema() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config = response.parse()
            assert_matches_type(object, config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_versions(self, client: Arbi) -> None:
        config = client.api.configs.retrieve_versions()
        assert_matches_type(ConfigRetrieveVersionsResponse, config, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve_versions(self, client: Arbi) -> None:
        response = client.api.configs.with_raw_response.retrieve_versions()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config = response.parse()
        assert_matches_type(ConfigRetrieveVersionsResponse, config, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
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

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncArbi) -> None:
        config = await async_client.api.configs.update()
        assert_matches_type(ConfigUpdateResponse, config, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncArbi) -> None:
        config = await async_client.api.configs.update(
            chunker={},
            document_date_extractor_llm={
                "api_type": "local",
                "max_char_size_to_answer": 0,
                "max_tokens": 0,
                "model_name": "MODEL_NAME",
                "system_instruction": "SYSTEM_INSTRUCTION",
                "temperature": 0,
            },
            embedder={
                "api_type": "local",
                "model_name": "MODEL_NAME",
            },
            model_citation={
                "max_numb_citations": 0,
                "min_char_size_to_answer": 0,
                "sim_model_name": "SIM_MODEL_NAME",
                "sim_threashold": 0,
            },
            parent_message_ext_id="parent_message_ext_id",
            parser={},
            query_llm={
                "api_type": "local",
                "max_char_size_to_answer": 0,
                "max_tokens": 0,
                "model_name": "MODEL_NAME",
                "system_instruction": "SYSTEM_INSTRUCTION",
                "temperature": 0,
            },
            reranker={
                "api_type": "local",
                "max_numb_of_chunks": 1,
                "model_name": "MODEL_NAME",
            },
            retriever={
                "group_size": 1000,
                "max_distinct_documents": 100,
                "max_total_chunks_to_retrieve": 100,
                "min_retrieval_sim_score": 0,
            },
            title="title",
            title_llm={
                "api_type": "local",
                "max_char_size_to_answer": 0,
                "max_tokens": 0,
                "model_name": "MODEL_NAME",
                "system_instruction": "SYSTEM_INSTRUCTION",
                "temperature": 0,
            },
        )
        assert_matches_type(ConfigUpdateResponse, config, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncArbi) -> None:
        response = await async_client.api.configs.with_raw_response.update()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config = await response.parse()
        assert_matches_type(ConfigUpdateResponse, config, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncArbi) -> None:
        async with async_client.api.configs.with_streaming_response.update() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config = await response.parse()
            assert_matches_type(ConfigUpdateResponse, config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_schema(self, async_client: AsyncArbi) -> None:
        config = await async_client.api.configs.retrieve_schema()
        assert_matches_type(object, config, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_schema(self, async_client: AsyncArbi) -> None:
        response = await async_client.api.configs.with_raw_response.retrieve_schema()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config = await response.parse()
        assert_matches_type(object, config, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_schema(self, async_client: AsyncArbi) -> None:
        async with async_client.api.configs.with_streaming_response.retrieve_schema() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config = await response.parse()
            assert_matches_type(object, config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_versions(self, async_client: AsyncArbi) -> None:
        config = await async_client.api.configs.retrieve_versions()
        assert_matches_type(ConfigRetrieveVersionsResponse, config, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_versions(self, async_client: AsyncArbi) -> None:
        response = await async_client.api.configs.with_raw_response.retrieve_versions()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config = await response.parse()
        assert_matches_type(ConfigRetrieveVersionsResponse, config, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_versions(self, async_client: AsyncArbi) -> None:
        async with async_client.api.configs.with_streaming_response.retrieve_versions() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config = await response.parse()
            assert_matches_type(ConfigRetrieveVersionsResponse, config, path=["response"])

        assert cast(Any, response.is_closed) is True
