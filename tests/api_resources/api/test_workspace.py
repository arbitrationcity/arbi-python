# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from arbi import Arbi, AsyncArbi
from tests.utils import assert_matches_type
from arbi.types.api import (
    WorkspaceResponse,
    WorkspaceShareResponse,
    WorkspaceDeleteResponse,
    WorkspaceListTagsResponse,
    WorkspaceListUsersResponse,
    WorkspaceRemoveUserResponse,
    WorkspaceListDoctagsResponse,
    WorkspaceListDocumentsResponse,
    WorkspaceRetrieveStatsResponse,
    WorkspaceListConversationsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestWorkspace:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Arbi) -> None:
        workspace = client.api.workspace.update(
            workspace_ext_id="wrk",
        )
        assert_matches_type(WorkspaceResponse, workspace, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params(self, client: Arbi) -> None:
        workspace = client.api.workspace.update(
            workspace_ext_id="wrk",
            description="description",
            name="name",
        )
        assert_matches_type(WorkspaceResponse, workspace, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: Arbi) -> None:
        response = client.api.workspace.with_raw_response.update(
            workspace_ext_id="wrk",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workspace = response.parse()
        assert_matches_type(WorkspaceResponse, workspace, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: Arbi) -> None:
        with client.api.workspace.with_streaming_response.update(
            workspace_ext_id="wrk",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workspace = response.parse()
            assert_matches_type(WorkspaceResponse, workspace, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update(self, client: Arbi) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_ext_id` but received ''"):
            client.api.workspace.with_raw_response.update(
                workspace_ext_id="",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Arbi) -> None:
        workspace = client.api.workspace.delete(
            "wrk",
        )
        assert_matches_type(WorkspaceDeleteResponse, workspace, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Arbi) -> None:
        response = client.api.workspace.with_raw_response.delete(
            "wrk",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workspace = response.parse()
        assert_matches_type(WorkspaceDeleteResponse, workspace, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Arbi) -> None:
        with client.api.workspace.with_streaming_response.delete(
            "wrk",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workspace = response.parse()
            assert_matches_type(WorkspaceDeleteResponse, workspace, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete(self, client: Arbi) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_ext_id` but received ''"):
            client.api.workspace.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_create_protected(self, client: Arbi) -> None:
        workspace = client.api.workspace.create_protected(
            name="name",
        )
        assert_matches_type(WorkspaceResponse, workspace, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_protected_with_all_params(self, client: Arbi) -> None:
        workspace = client.api.workspace.create_protected(
            name="name",
            description="description",
        )
        assert_matches_type(WorkspaceResponse, workspace, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create_protected(self, client: Arbi) -> None:
        response = client.api.workspace.with_raw_response.create_protected(
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workspace = response.parse()
        assert_matches_type(WorkspaceResponse, workspace, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create_protected(self, client: Arbi) -> None:
        with client.api.workspace.with_streaming_response.create_protected(
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workspace = response.parse()
            assert_matches_type(WorkspaceResponse, workspace, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_list_conversations(self, client: Arbi) -> None:
        workspace = client.api.workspace.list_conversations(
            "wrk",
        )
        assert_matches_type(WorkspaceListConversationsResponse, workspace, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list_conversations(self, client: Arbi) -> None:
        response = client.api.workspace.with_raw_response.list_conversations(
            "wrk",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workspace = response.parse()
        assert_matches_type(WorkspaceListConversationsResponse, workspace, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list_conversations(self, client: Arbi) -> None:
        with client.api.workspace.with_streaming_response.list_conversations(
            "wrk",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workspace = response.parse()
            assert_matches_type(WorkspaceListConversationsResponse, workspace, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_list_conversations(self, client: Arbi) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_ext_id` but received ''"):
            client.api.workspace.with_raw_response.list_conversations(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_list_doctags(self, client: Arbi) -> None:
        workspace = client.api.workspace.list_doctags(
            "wrk",
        )
        assert_matches_type(WorkspaceListDoctagsResponse, workspace, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list_doctags(self, client: Arbi) -> None:
        response = client.api.workspace.with_raw_response.list_doctags(
            "wrk",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workspace = response.parse()
        assert_matches_type(WorkspaceListDoctagsResponse, workspace, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list_doctags(self, client: Arbi) -> None:
        with client.api.workspace.with_streaming_response.list_doctags(
            "wrk",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workspace = response.parse()
            assert_matches_type(WorkspaceListDoctagsResponse, workspace, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_list_doctags(self, client: Arbi) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_ext_id` but received ''"):
            client.api.workspace.with_raw_response.list_doctags(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_list_documents(self, client: Arbi) -> None:
        workspace = client.api.workspace.list_documents(
            "wrk",
        )
        assert_matches_type(WorkspaceListDocumentsResponse, workspace, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list_documents(self, client: Arbi) -> None:
        response = client.api.workspace.with_raw_response.list_documents(
            "wrk",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workspace = response.parse()
        assert_matches_type(WorkspaceListDocumentsResponse, workspace, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list_documents(self, client: Arbi) -> None:
        with client.api.workspace.with_streaming_response.list_documents(
            "wrk",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workspace = response.parse()
            assert_matches_type(WorkspaceListDocumentsResponse, workspace, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_list_documents(self, client: Arbi) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_ext_id` but received ''"):
            client.api.workspace.with_raw_response.list_documents(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_list_tags(self, client: Arbi) -> None:
        workspace = client.api.workspace.list_tags(
            "wrk",
        )
        assert_matches_type(WorkspaceListTagsResponse, workspace, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list_tags(self, client: Arbi) -> None:
        response = client.api.workspace.with_raw_response.list_tags(
            "wrk",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workspace = response.parse()
        assert_matches_type(WorkspaceListTagsResponse, workspace, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list_tags(self, client: Arbi) -> None:
        with client.api.workspace.with_streaming_response.list_tags(
            "wrk",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workspace = response.parse()
            assert_matches_type(WorkspaceListTagsResponse, workspace, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_list_tags(self, client: Arbi) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_ext_id` but received ''"):
            client.api.workspace.with_raw_response.list_tags(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_list_users(self, client: Arbi) -> None:
        workspace = client.api.workspace.list_users(
            "wrk",
        )
        assert_matches_type(WorkspaceListUsersResponse, workspace, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list_users(self, client: Arbi) -> None:
        response = client.api.workspace.with_raw_response.list_users(
            "wrk",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workspace = response.parse()
        assert_matches_type(WorkspaceListUsersResponse, workspace, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list_users(self, client: Arbi) -> None:
        with client.api.workspace.with_streaming_response.list_users(
            "wrk",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workspace = response.parse()
            assert_matches_type(WorkspaceListUsersResponse, workspace, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_list_users(self, client: Arbi) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_ext_id` but received ''"):
            client.api.workspace.with_raw_response.list_users(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_remove_user(self, client: Arbi) -> None:
        workspace = client.api.workspace.remove_user(
            workspace_ext_id="wrk",
            user_ext_id="user_ext_id",
        )
        assert_matches_type(WorkspaceRemoveUserResponse, workspace, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_remove_user(self, client: Arbi) -> None:
        response = client.api.workspace.with_raw_response.remove_user(
            workspace_ext_id="wrk",
            user_ext_id="user_ext_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workspace = response.parse()
        assert_matches_type(WorkspaceRemoveUserResponse, workspace, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_remove_user(self, client: Arbi) -> None:
        with client.api.workspace.with_streaming_response.remove_user(
            workspace_ext_id="wrk",
            user_ext_id="user_ext_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workspace = response.parse()
            assert_matches_type(WorkspaceRemoveUserResponse, workspace, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_remove_user(self, client: Arbi) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_ext_id` but received ''"):
            client.api.workspace.with_raw_response.remove_user(
                workspace_ext_id="",
                user_ext_id="user_ext_id",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve_stats(self, client: Arbi) -> None:
        workspace = client.api.workspace.retrieve_stats(
            "wrk",
        )
        assert_matches_type(WorkspaceRetrieveStatsResponse, workspace, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve_stats(self, client: Arbi) -> None:
        response = client.api.workspace.with_raw_response.retrieve_stats(
            "wrk",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workspace = response.parse()
        assert_matches_type(WorkspaceRetrieveStatsResponse, workspace, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve_stats(self, client: Arbi) -> None:
        with client.api.workspace.with_streaming_response.retrieve_stats(
            "wrk",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workspace = response.parse()
            assert_matches_type(WorkspaceRetrieveStatsResponse, workspace, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_retrieve_stats(self, client: Arbi) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_ext_id` but received ''"):
            client.api.workspace.with_raw_response.retrieve_stats(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_share(self, client: Arbi) -> None:
        workspace = client.api.workspace.share(
            workspace_ext_id="wrk",
            recipient_email="recipient_email",
        )
        assert_matches_type(WorkspaceShareResponse, workspace, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_share(self, client: Arbi) -> None:
        response = client.api.workspace.with_raw_response.share(
            workspace_ext_id="wrk",
            recipient_email="recipient_email",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workspace = response.parse()
        assert_matches_type(WorkspaceShareResponse, workspace, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_share(self, client: Arbi) -> None:
        with client.api.workspace.with_streaming_response.share(
            workspace_ext_id="wrk",
            recipient_email="recipient_email",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workspace = response.parse()
            assert_matches_type(WorkspaceShareResponse, workspace, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_share(self, client: Arbi) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_ext_id` but received ''"):
            client.api.workspace.with_raw_response.share(
                workspace_ext_id="",
                recipient_email="recipient_email",
            )


class TestAsyncWorkspace:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncArbi) -> None:
        workspace = await async_client.api.workspace.update(
            workspace_ext_id="wrk",
        )
        assert_matches_type(WorkspaceResponse, workspace, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncArbi) -> None:
        workspace = await async_client.api.workspace.update(
            workspace_ext_id="wrk",
            description="description",
            name="name",
        )
        assert_matches_type(WorkspaceResponse, workspace, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncArbi) -> None:
        response = await async_client.api.workspace.with_raw_response.update(
            workspace_ext_id="wrk",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workspace = await response.parse()
        assert_matches_type(WorkspaceResponse, workspace, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncArbi) -> None:
        async with async_client.api.workspace.with_streaming_response.update(
            workspace_ext_id="wrk",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workspace = await response.parse()
            assert_matches_type(WorkspaceResponse, workspace, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update(self, async_client: AsyncArbi) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_ext_id` but received ''"):
            await async_client.api.workspace.with_raw_response.update(
                workspace_ext_id="",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncArbi) -> None:
        workspace = await async_client.api.workspace.delete(
            "wrk",
        )
        assert_matches_type(WorkspaceDeleteResponse, workspace, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncArbi) -> None:
        response = await async_client.api.workspace.with_raw_response.delete(
            "wrk",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workspace = await response.parse()
        assert_matches_type(WorkspaceDeleteResponse, workspace, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncArbi) -> None:
        async with async_client.api.workspace.with_streaming_response.delete(
            "wrk",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workspace = await response.parse()
            assert_matches_type(WorkspaceDeleteResponse, workspace, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncArbi) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_ext_id` but received ''"):
            await async_client.api.workspace.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_protected(self, async_client: AsyncArbi) -> None:
        workspace = await async_client.api.workspace.create_protected(
            name="name",
        )
        assert_matches_type(WorkspaceResponse, workspace, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_protected_with_all_params(self, async_client: AsyncArbi) -> None:
        workspace = await async_client.api.workspace.create_protected(
            name="name",
            description="description",
        )
        assert_matches_type(WorkspaceResponse, workspace, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create_protected(self, async_client: AsyncArbi) -> None:
        response = await async_client.api.workspace.with_raw_response.create_protected(
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workspace = await response.parse()
        assert_matches_type(WorkspaceResponse, workspace, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create_protected(self, async_client: AsyncArbi) -> None:
        async with async_client.api.workspace.with_streaming_response.create_protected(
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workspace = await response.parse()
            assert_matches_type(WorkspaceResponse, workspace, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_conversations(self, async_client: AsyncArbi) -> None:
        workspace = await async_client.api.workspace.list_conversations(
            "wrk",
        )
        assert_matches_type(WorkspaceListConversationsResponse, workspace, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list_conversations(self, async_client: AsyncArbi) -> None:
        response = await async_client.api.workspace.with_raw_response.list_conversations(
            "wrk",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workspace = await response.parse()
        assert_matches_type(WorkspaceListConversationsResponse, workspace, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list_conversations(self, async_client: AsyncArbi) -> None:
        async with async_client.api.workspace.with_streaming_response.list_conversations(
            "wrk",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workspace = await response.parse()
            assert_matches_type(WorkspaceListConversationsResponse, workspace, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_list_conversations(self, async_client: AsyncArbi) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_ext_id` but received ''"):
            await async_client.api.workspace.with_raw_response.list_conversations(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_doctags(self, async_client: AsyncArbi) -> None:
        workspace = await async_client.api.workspace.list_doctags(
            "wrk",
        )
        assert_matches_type(WorkspaceListDoctagsResponse, workspace, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list_doctags(self, async_client: AsyncArbi) -> None:
        response = await async_client.api.workspace.with_raw_response.list_doctags(
            "wrk",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workspace = await response.parse()
        assert_matches_type(WorkspaceListDoctagsResponse, workspace, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list_doctags(self, async_client: AsyncArbi) -> None:
        async with async_client.api.workspace.with_streaming_response.list_doctags(
            "wrk",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workspace = await response.parse()
            assert_matches_type(WorkspaceListDoctagsResponse, workspace, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_list_doctags(self, async_client: AsyncArbi) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_ext_id` but received ''"):
            await async_client.api.workspace.with_raw_response.list_doctags(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_documents(self, async_client: AsyncArbi) -> None:
        workspace = await async_client.api.workspace.list_documents(
            "wrk",
        )
        assert_matches_type(WorkspaceListDocumentsResponse, workspace, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list_documents(self, async_client: AsyncArbi) -> None:
        response = await async_client.api.workspace.with_raw_response.list_documents(
            "wrk",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workspace = await response.parse()
        assert_matches_type(WorkspaceListDocumentsResponse, workspace, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list_documents(self, async_client: AsyncArbi) -> None:
        async with async_client.api.workspace.with_streaming_response.list_documents(
            "wrk",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workspace = await response.parse()
            assert_matches_type(WorkspaceListDocumentsResponse, workspace, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_list_documents(self, async_client: AsyncArbi) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_ext_id` but received ''"):
            await async_client.api.workspace.with_raw_response.list_documents(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_tags(self, async_client: AsyncArbi) -> None:
        workspace = await async_client.api.workspace.list_tags(
            "wrk",
        )
        assert_matches_type(WorkspaceListTagsResponse, workspace, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list_tags(self, async_client: AsyncArbi) -> None:
        response = await async_client.api.workspace.with_raw_response.list_tags(
            "wrk",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workspace = await response.parse()
        assert_matches_type(WorkspaceListTagsResponse, workspace, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list_tags(self, async_client: AsyncArbi) -> None:
        async with async_client.api.workspace.with_streaming_response.list_tags(
            "wrk",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workspace = await response.parse()
            assert_matches_type(WorkspaceListTagsResponse, workspace, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_list_tags(self, async_client: AsyncArbi) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_ext_id` but received ''"):
            await async_client.api.workspace.with_raw_response.list_tags(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_users(self, async_client: AsyncArbi) -> None:
        workspace = await async_client.api.workspace.list_users(
            "wrk",
        )
        assert_matches_type(WorkspaceListUsersResponse, workspace, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list_users(self, async_client: AsyncArbi) -> None:
        response = await async_client.api.workspace.with_raw_response.list_users(
            "wrk",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workspace = await response.parse()
        assert_matches_type(WorkspaceListUsersResponse, workspace, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list_users(self, async_client: AsyncArbi) -> None:
        async with async_client.api.workspace.with_streaming_response.list_users(
            "wrk",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workspace = await response.parse()
            assert_matches_type(WorkspaceListUsersResponse, workspace, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_list_users(self, async_client: AsyncArbi) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_ext_id` but received ''"):
            await async_client.api.workspace.with_raw_response.list_users(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_remove_user(self, async_client: AsyncArbi) -> None:
        workspace = await async_client.api.workspace.remove_user(
            workspace_ext_id="wrk",
            user_ext_id="user_ext_id",
        )
        assert_matches_type(WorkspaceRemoveUserResponse, workspace, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_remove_user(self, async_client: AsyncArbi) -> None:
        response = await async_client.api.workspace.with_raw_response.remove_user(
            workspace_ext_id="wrk",
            user_ext_id="user_ext_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workspace = await response.parse()
        assert_matches_type(WorkspaceRemoveUserResponse, workspace, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_remove_user(self, async_client: AsyncArbi) -> None:
        async with async_client.api.workspace.with_streaming_response.remove_user(
            workspace_ext_id="wrk",
            user_ext_id="user_ext_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workspace = await response.parse()
            assert_matches_type(WorkspaceRemoveUserResponse, workspace, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_remove_user(self, async_client: AsyncArbi) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_ext_id` but received ''"):
            await async_client.api.workspace.with_raw_response.remove_user(
                workspace_ext_id="",
                user_ext_id="user_ext_id",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve_stats(self, async_client: AsyncArbi) -> None:
        workspace = await async_client.api.workspace.retrieve_stats(
            "wrk",
        )
        assert_matches_type(WorkspaceRetrieveStatsResponse, workspace, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve_stats(self, async_client: AsyncArbi) -> None:
        response = await async_client.api.workspace.with_raw_response.retrieve_stats(
            "wrk",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workspace = await response.parse()
        assert_matches_type(WorkspaceRetrieveStatsResponse, workspace, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve_stats(self, async_client: AsyncArbi) -> None:
        async with async_client.api.workspace.with_streaming_response.retrieve_stats(
            "wrk",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workspace = await response.parse()
            assert_matches_type(WorkspaceRetrieveStatsResponse, workspace, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_retrieve_stats(self, async_client: AsyncArbi) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_ext_id` but received ''"):
            await async_client.api.workspace.with_raw_response.retrieve_stats(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_share(self, async_client: AsyncArbi) -> None:
        workspace = await async_client.api.workspace.share(
            workspace_ext_id="wrk",
            recipient_email="recipient_email",
        )
        assert_matches_type(WorkspaceShareResponse, workspace, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_share(self, async_client: AsyncArbi) -> None:
        response = await async_client.api.workspace.with_raw_response.share(
            workspace_ext_id="wrk",
            recipient_email="recipient_email",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workspace = await response.parse()
        assert_matches_type(WorkspaceShareResponse, workspace, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_share(self, async_client: AsyncArbi) -> None:
        async with async_client.api.workspace.with_streaming_response.share(
            workspace_ext_id="wrk",
            recipient_email="recipient_email",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workspace = await response.parse()
            assert_matches_type(WorkspaceShareResponse, workspace, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_share(self, async_client: AsyncArbi) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_ext_id` but received ''"):
            await async_client.api.workspace.with_raw_response.share(
                workspace_ext_id="",
                recipient_email="recipient_email",
            )
