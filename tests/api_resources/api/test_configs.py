# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from arbi import Arbi, AsyncArbi
from tests.utils import assert_matches_type
from arbi.types.api import (
    ConfigDeleteResponse,
    ConfigUpdateResponse,
    ConfigRetrieveResponse,
    ConfigRetrieveSchemaResponse,
    ConfigRetrieveVersionsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestConfigs:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve(self, client: Arbi) -> None:
        config = client.api.configs.retrieve(
            "config_path",
        )
        assert_matches_type(ConfigRetrieveResponse, config, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve(self, client: Arbi) -> None:
        response = client.api.configs.with_raw_response.retrieve(
            "config_path",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config = response.parse()
        assert_matches_type(ConfigRetrieveResponse, config, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve(self, client: Arbi) -> None:
        with client.api.configs.with_streaming_response.retrieve(
            "config_path",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config = response.parse()
            assert_matches_type(ConfigRetrieveResponse, config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_retrieve(self, client: Arbi) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `config_path` but received ''"):
            client.api.configs.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Arbi) -> None:
        config = client.api.configs.update()
        assert_matches_type(ConfigUpdateResponse, config, path=["response"])

    @pytest.mark.skip()
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
            filename_suffix="filename_suffix",
            model_citation={
                "model_name": "MODEL_NAME",
                "sim_threashold": 0,
            },
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

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: Arbi) -> None:
        response = client.api.configs.with_raw_response.update()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config = response.parse()
        assert_matches_type(ConfigUpdateResponse, config, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: Arbi) -> None:
        with client.api.configs.with_streaming_response.update() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config = response.parse()
            assert_matches_type(ConfigUpdateResponse, config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Arbi) -> None:
        config = client.api.configs.delete(
            "filename",
        )
        assert_matches_type(ConfigDeleteResponse, config, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Arbi) -> None:
        response = client.api.configs.with_raw_response.delete(
            "filename",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config = response.parse()
        assert_matches_type(ConfigDeleteResponse, config, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Arbi) -> None:
        with client.api.configs.with_streaming_response.delete(
            "filename",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config = response.parse()
            assert_matches_type(ConfigDeleteResponse, config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete(self, client: Arbi) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `filename` but received ''"):
            client.api.configs.with_raw_response.delete(
                "",
            )

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
    async def test_method_retrieve(self, async_client: AsyncArbi) -> None:
        config = await async_client.api.configs.retrieve(
            "config_path",
        )
        assert_matches_type(ConfigRetrieveResponse, config, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncArbi) -> None:
        response = await async_client.api.configs.with_raw_response.retrieve(
            "config_path",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config = await response.parse()
        assert_matches_type(ConfigRetrieveResponse, config, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncArbi) -> None:
        async with async_client.api.configs.with_streaming_response.retrieve(
            "config_path",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config = await response.parse()
            assert_matches_type(ConfigRetrieveResponse, config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncArbi) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `config_path` but received ''"):
            await async_client.api.configs.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncArbi) -> None:
        config = await async_client.api.configs.update()
        assert_matches_type(ConfigUpdateResponse, config, path=["response"])

    @pytest.mark.skip()
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
            filename_suffix="filename_suffix",
            model_citation={
                "model_name": "MODEL_NAME",
                "sim_threashold": 0,
            },
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

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncArbi) -> None:
        response = await async_client.api.configs.with_raw_response.update()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config = await response.parse()
        assert_matches_type(ConfigUpdateResponse, config, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncArbi) -> None:
        async with async_client.api.configs.with_streaming_response.update() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config = await response.parse()
            assert_matches_type(ConfigUpdateResponse, config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncArbi) -> None:
        config = await async_client.api.configs.delete(
            "filename",
        )
        assert_matches_type(ConfigDeleteResponse, config, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncArbi) -> None:
        response = await async_client.api.configs.with_raw_response.delete(
            "filename",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config = await response.parse()
        assert_matches_type(ConfigDeleteResponse, config, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncArbi) -> None:
        async with async_client.api.configs.with_streaming_response.delete(
            "filename",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config = await response.parse()
            assert_matches_type(ConfigDeleteResponse, config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncArbi) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `filename` but received ''"):
            await async_client.api.configs.with_raw_response.delete(
                "",
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
