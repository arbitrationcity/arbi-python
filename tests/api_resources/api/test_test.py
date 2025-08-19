# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from arbi import Arbi, AsyncArbi
from tests.utils import assert_matches_type
from arbi.types.api import SimpleResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTest:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_test_endpoint_1(self, client: Arbi) -> None:
        test = client.api.test.test_endpoint_1()
        assert_matches_type(SimpleResponse, test, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_test_endpoint_1(self, client: Arbi) -> None:
        response = client.api.test.with_raw_response.test_endpoint_1()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        test = response.parse()
        assert_matches_type(SimpleResponse, test, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_test_endpoint_1(self, client: Arbi) -> None:
        with client.api.test.with_streaming_response.test_endpoint_1() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            test = response.parse()
            assert_matches_type(SimpleResponse, test, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_test_endpoint_10(self, client: Arbi) -> None:
        test = client.api.test.test_endpoint_10()
        assert_matches_type(SimpleResponse, test, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_test_endpoint_10(self, client: Arbi) -> None:
        response = client.api.test.with_raw_response.test_endpoint_10()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        test = response.parse()
        assert_matches_type(SimpleResponse, test, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_test_endpoint_10(self, client: Arbi) -> None:
        with client.api.test.with_streaming_response.test_endpoint_10() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            test = response.parse()
            assert_matches_type(SimpleResponse, test, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_test_endpoint_11(self, client: Arbi) -> None:
        test = client.api.test.test_endpoint_11()
        assert_matches_type(SimpleResponse, test, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_test_endpoint_11(self, client: Arbi) -> None:
        response = client.api.test.with_raw_response.test_endpoint_11()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        test = response.parse()
        assert_matches_type(SimpleResponse, test, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_test_endpoint_11(self, client: Arbi) -> None:
        with client.api.test.with_streaming_response.test_endpoint_11() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            test = response.parse()
            assert_matches_type(SimpleResponse, test, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_test_endpoint_12(self, client: Arbi) -> None:
        test = client.api.test.test_endpoint_12()
        assert_matches_type(SimpleResponse, test, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_test_endpoint_12(self, client: Arbi) -> None:
        response = client.api.test.with_raw_response.test_endpoint_12()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        test = response.parse()
        assert_matches_type(SimpleResponse, test, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_test_endpoint_12(self, client: Arbi) -> None:
        with client.api.test.with_streaming_response.test_endpoint_12() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            test = response.parse()
            assert_matches_type(SimpleResponse, test, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_test_endpoint_13(self, client: Arbi) -> None:
        test = client.api.test.test_endpoint_13()
        assert_matches_type(SimpleResponse, test, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_test_endpoint_13(self, client: Arbi) -> None:
        response = client.api.test.with_raw_response.test_endpoint_13()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        test = response.parse()
        assert_matches_type(SimpleResponse, test, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_test_endpoint_13(self, client: Arbi) -> None:
        with client.api.test.with_streaming_response.test_endpoint_13() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            test = response.parse()
            assert_matches_type(SimpleResponse, test, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_test_endpoint_14(self, client: Arbi) -> None:
        test = client.api.test.test_endpoint_14()
        assert_matches_type(SimpleResponse, test, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_test_endpoint_14(self, client: Arbi) -> None:
        response = client.api.test.with_raw_response.test_endpoint_14()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        test = response.parse()
        assert_matches_type(SimpleResponse, test, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_test_endpoint_14(self, client: Arbi) -> None:
        with client.api.test.with_streaming_response.test_endpoint_14() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            test = response.parse()
            assert_matches_type(SimpleResponse, test, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_test_endpoint_15(self, client: Arbi) -> None:
        test = client.api.test.test_endpoint_15()
        assert_matches_type(SimpleResponse, test, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_test_endpoint_15(self, client: Arbi) -> None:
        response = client.api.test.with_raw_response.test_endpoint_15()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        test = response.parse()
        assert_matches_type(SimpleResponse, test, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_test_endpoint_15(self, client: Arbi) -> None:
        with client.api.test.with_streaming_response.test_endpoint_15() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            test = response.parse()
            assert_matches_type(SimpleResponse, test, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_test_endpoint_16(self, client: Arbi) -> None:
        test = client.api.test.test_endpoint_16()
        assert_matches_type(SimpleResponse, test, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_test_endpoint_16(self, client: Arbi) -> None:
        response = client.api.test.with_raw_response.test_endpoint_16()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        test = response.parse()
        assert_matches_type(SimpleResponse, test, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_test_endpoint_16(self, client: Arbi) -> None:
        with client.api.test.with_streaming_response.test_endpoint_16() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            test = response.parse()
            assert_matches_type(SimpleResponse, test, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_test_endpoint_17(self, client: Arbi) -> None:
        test = client.api.test.test_endpoint_17()
        assert_matches_type(SimpleResponse, test, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_test_endpoint_17(self, client: Arbi) -> None:
        response = client.api.test.with_raw_response.test_endpoint_17()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        test = response.parse()
        assert_matches_type(SimpleResponse, test, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_test_endpoint_17(self, client: Arbi) -> None:
        with client.api.test.with_streaming_response.test_endpoint_17() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            test = response.parse()
            assert_matches_type(SimpleResponse, test, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_test_endpoint_18(self, client: Arbi) -> None:
        test = client.api.test.test_endpoint_18()
        assert_matches_type(SimpleResponse, test, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_test_endpoint_18(self, client: Arbi) -> None:
        response = client.api.test.with_raw_response.test_endpoint_18()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        test = response.parse()
        assert_matches_type(SimpleResponse, test, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_test_endpoint_18(self, client: Arbi) -> None:
        with client.api.test.with_streaming_response.test_endpoint_18() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            test = response.parse()
            assert_matches_type(SimpleResponse, test, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_test_endpoint_19(self, client: Arbi) -> None:
        test = client.api.test.test_endpoint_19()
        assert_matches_type(SimpleResponse, test, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_test_endpoint_19(self, client: Arbi) -> None:
        response = client.api.test.with_raw_response.test_endpoint_19()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        test = response.parse()
        assert_matches_type(SimpleResponse, test, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_test_endpoint_19(self, client: Arbi) -> None:
        with client.api.test.with_streaming_response.test_endpoint_19() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            test = response.parse()
            assert_matches_type(SimpleResponse, test, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_test_endpoint_2(self, client: Arbi) -> None:
        test = client.api.test.test_endpoint_2()
        assert_matches_type(SimpleResponse, test, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_test_endpoint_2(self, client: Arbi) -> None:
        response = client.api.test.with_raw_response.test_endpoint_2()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        test = response.parse()
        assert_matches_type(SimpleResponse, test, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_test_endpoint_2(self, client: Arbi) -> None:
        with client.api.test.with_streaming_response.test_endpoint_2() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            test = response.parse()
            assert_matches_type(SimpleResponse, test, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_test_endpoint_20(self, client: Arbi) -> None:
        test = client.api.test.test_endpoint_20()
        assert_matches_type(SimpleResponse, test, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_test_endpoint_20(self, client: Arbi) -> None:
        response = client.api.test.with_raw_response.test_endpoint_20()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        test = response.parse()
        assert_matches_type(SimpleResponse, test, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_test_endpoint_20(self, client: Arbi) -> None:
        with client.api.test.with_streaming_response.test_endpoint_20() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            test = response.parse()
            assert_matches_type(SimpleResponse, test, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_test_endpoint_21(self, client: Arbi) -> None:
        test = client.api.test.test_endpoint_21()
        assert_matches_type(SimpleResponse, test, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_test_endpoint_21(self, client: Arbi) -> None:
        response = client.api.test.with_raw_response.test_endpoint_21()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        test = response.parse()
        assert_matches_type(SimpleResponse, test, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_test_endpoint_21(self, client: Arbi) -> None:
        with client.api.test.with_streaming_response.test_endpoint_21() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            test = response.parse()
            assert_matches_type(SimpleResponse, test, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_test_endpoint_22(self, client: Arbi) -> None:
        test = client.api.test.test_endpoint_22()
        assert_matches_type(SimpleResponse, test, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_test_endpoint_22(self, client: Arbi) -> None:
        response = client.api.test.with_raw_response.test_endpoint_22()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        test = response.parse()
        assert_matches_type(SimpleResponse, test, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_test_endpoint_22(self, client: Arbi) -> None:
        with client.api.test.with_streaming_response.test_endpoint_22() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            test = response.parse()
            assert_matches_type(SimpleResponse, test, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_test_endpoint_23(self, client: Arbi) -> None:
        test = client.api.test.test_endpoint_23()
        assert_matches_type(SimpleResponse, test, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_test_endpoint_23(self, client: Arbi) -> None:
        response = client.api.test.with_raw_response.test_endpoint_23()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        test = response.parse()
        assert_matches_type(SimpleResponse, test, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_test_endpoint_23(self, client: Arbi) -> None:
        with client.api.test.with_streaming_response.test_endpoint_23() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            test = response.parse()
            assert_matches_type(SimpleResponse, test, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_test_endpoint_24(self, client: Arbi) -> None:
        test = client.api.test.test_endpoint_24()
        assert_matches_type(SimpleResponse, test, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_test_endpoint_24(self, client: Arbi) -> None:
        response = client.api.test.with_raw_response.test_endpoint_24()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        test = response.parse()
        assert_matches_type(SimpleResponse, test, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_test_endpoint_24(self, client: Arbi) -> None:
        with client.api.test.with_streaming_response.test_endpoint_24() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            test = response.parse()
            assert_matches_type(SimpleResponse, test, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_test_endpoint_25(self, client: Arbi) -> None:
        test = client.api.test.test_endpoint_25()
        assert_matches_type(SimpleResponse, test, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_test_endpoint_25(self, client: Arbi) -> None:
        response = client.api.test.with_raw_response.test_endpoint_25()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        test = response.parse()
        assert_matches_type(SimpleResponse, test, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_test_endpoint_25(self, client: Arbi) -> None:
        with client.api.test.with_streaming_response.test_endpoint_25() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            test = response.parse()
            assert_matches_type(SimpleResponse, test, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_test_endpoint_26(self, client: Arbi) -> None:
        test = client.api.test.test_endpoint_26()
        assert_matches_type(SimpleResponse, test, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_test_endpoint_26(self, client: Arbi) -> None:
        response = client.api.test.with_raw_response.test_endpoint_26()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        test = response.parse()
        assert_matches_type(SimpleResponse, test, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_test_endpoint_26(self, client: Arbi) -> None:
        with client.api.test.with_streaming_response.test_endpoint_26() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            test = response.parse()
            assert_matches_type(SimpleResponse, test, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_test_endpoint_27(self, client: Arbi) -> None:
        test = client.api.test.test_endpoint_27()
        assert_matches_type(SimpleResponse, test, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_test_endpoint_27(self, client: Arbi) -> None:
        response = client.api.test.with_raw_response.test_endpoint_27()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        test = response.parse()
        assert_matches_type(SimpleResponse, test, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_test_endpoint_27(self, client: Arbi) -> None:
        with client.api.test.with_streaming_response.test_endpoint_27() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            test = response.parse()
            assert_matches_type(SimpleResponse, test, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_test_endpoint_28(self, client: Arbi) -> None:
        test = client.api.test.test_endpoint_28()
        assert_matches_type(SimpleResponse, test, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_test_endpoint_28(self, client: Arbi) -> None:
        response = client.api.test.with_raw_response.test_endpoint_28()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        test = response.parse()
        assert_matches_type(SimpleResponse, test, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_test_endpoint_28(self, client: Arbi) -> None:
        with client.api.test.with_streaming_response.test_endpoint_28() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            test = response.parse()
            assert_matches_type(SimpleResponse, test, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_test_endpoint_29(self, client: Arbi) -> None:
        test = client.api.test.test_endpoint_29()
        assert_matches_type(SimpleResponse, test, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_test_endpoint_29(self, client: Arbi) -> None:
        response = client.api.test.with_raw_response.test_endpoint_29()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        test = response.parse()
        assert_matches_type(SimpleResponse, test, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_test_endpoint_29(self, client: Arbi) -> None:
        with client.api.test.with_streaming_response.test_endpoint_29() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            test = response.parse()
            assert_matches_type(SimpleResponse, test, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_test_endpoint_3(self, client: Arbi) -> None:
        test = client.api.test.test_endpoint_3()
        assert_matches_type(SimpleResponse, test, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_test_endpoint_3(self, client: Arbi) -> None:
        response = client.api.test.with_raw_response.test_endpoint_3()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        test = response.parse()
        assert_matches_type(SimpleResponse, test, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_test_endpoint_3(self, client: Arbi) -> None:
        with client.api.test.with_streaming_response.test_endpoint_3() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            test = response.parse()
            assert_matches_type(SimpleResponse, test, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_test_endpoint_30(self, client: Arbi) -> None:
        test = client.api.test.test_endpoint_30()
        assert_matches_type(SimpleResponse, test, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_test_endpoint_30(self, client: Arbi) -> None:
        response = client.api.test.with_raw_response.test_endpoint_30()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        test = response.parse()
        assert_matches_type(SimpleResponse, test, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_test_endpoint_30(self, client: Arbi) -> None:
        with client.api.test.with_streaming_response.test_endpoint_30() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            test = response.parse()
            assert_matches_type(SimpleResponse, test, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_test_endpoint_4(self, client: Arbi) -> None:
        test = client.api.test.test_endpoint_4()
        assert_matches_type(SimpleResponse, test, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_test_endpoint_4(self, client: Arbi) -> None:
        response = client.api.test.with_raw_response.test_endpoint_4()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        test = response.parse()
        assert_matches_type(SimpleResponse, test, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_test_endpoint_4(self, client: Arbi) -> None:
        with client.api.test.with_streaming_response.test_endpoint_4() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            test = response.parse()
            assert_matches_type(SimpleResponse, test, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_test_endpoint_5(self, client: Arbi) -> None:
        test = client.api.test.test_endpoint_5()
        assert_matches_type(SimpleResponse, test, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_test_endpoint_5(self, client: Arbi) -> None:
        response = client.api.test.with_raw_response.test_endpoint_5()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        test = response.parse()
        assert_matches_type(SimpleResponse, test, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_test_endpoint_5(self, client: Arbi) -> None:
        with client.api.test.with_streaming_response.test_endpoint_5() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            test = response.parse()
            assert_matches_type(SimpleResponse, test, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_test_endpoint_6(self, client: Arbi) -> None:
        test = client.api.test.test_endpoint_6()
        assert_matches_type(SimpleResponse, test, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_test_endpoint_6(self, client: Arbi) -> None:
        response = client.api.test.with_raw_response.test_endpoint_6()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        test = response.parse()
        assert_matches_type(SimpleResponse, test, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_test_endpoint_6(self, client: Arbi) -> None:
        with client.api.test.with_streaming_response.test_endpoint_6() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            test = response.parse()
            assert_matches_type(SimpleResponse, test, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_test_endpoint_7(self, client: Arbi) -> None:
        test = client.api.test.test_endpoint_7()
        assert_matches_type(SimpleResponse, test, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_test_endpoint_7(self, client: Arbi) -> None:
        response = client.api.test.with_raw_response.test_endpoint_7()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        test = response.parse()
        assert_matches_type(SimpleResponse, test, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_test_endpoint_7(self, client: Arbi) -> None:
        with client.api.test.with_streaming_response.test_endpoint_7() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            test = response.parse()
            assert_matches_type(SimpleResponse, test, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_test_endpoint_8(self, client: Arbi) -> None:
        test = client.api.test.test_endpoint_8()
        assert_matches_type(SimpleResponse, test, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_test_endpoint_8(self, client: Arbi) -> None:
        response = client.api.test.with_raw_response.test_endpoint_8()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        test = response.parse()
        assert_matches_type(SimpleResponse, test, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_test_endpoint_8(self, client: Arbi) -> None:
        with client.api.test.with_streaming_response.test_endpoint_8() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            test = response.parse()
            assert_matches_type(SimpleResponse, test, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_test_endpoint_9(self, client: Arbi) -> None:
        test = client.api.test.test_endpoint_9()
        assert_matches_type(SimpleResponse, test, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_test_endpoint_9(self, client: Arbi) -> None:
        response = client.api.test.with_raw_response.test_endpoint_9()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        test = response.parse()
        assert_matches_type(SimpleResponse, test, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_test_endpoint_9(self, client: Arbi) -> None:
        with client.api.test.with_streaming_response.test_endpoint_9() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            test = response.parse()
            assert_matches_type(SimpleResponse, test, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncTest:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_test_endpoint_1(self, async_client: AsyncArbi) -> None:
        test = await async_client.api.test.test_endpoint_1()
        assert_matches_type(SimpleResponse, test, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_test_endpoint_1(self, async_client: AsyncArbi) -> None:
        response = await async_client.api.test.with_raw_response.test_endpoint_1()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        test = await response.parse()
        assert_matches_type(SimpleResponse, test, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_test_endpoint_1(self, async_client: AsyncArbi) -> None:
        async with async_client.api.test.with_streaming_response.test_endpoint_1() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            test = await response.parse()
            assert_matches_type(SimpleResponse, test, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_test_endpoint_10(self, async_client: AsyncArbi) -> None:
        test = await async_client.api.test.test_endpoint_10()
        assert_matches_type(SimpleResponse, test, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_test_endpoint_10(self, async_client: AsyncArbi) -> None:
        response = await async_client.api.test.with_raw_response.test_endpoint_10()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        test = await response.parse()
        assert_matches_type(SimpleResponse, test, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_test_endpoint_10(self, async_client: AsyncArbi) -> None:
        async with async_client.api.test.with_streaming_response.test_endpoint_10() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            test = await response.parse()
            assert_matches_type(SimpleResponse, test, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_test_endpoint_11(self, async_client: AsyncArbi) -> None:
        test = await async_client.api.test.test_endpoint_11()
        assert_matches_type(SimpleResponse, test, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_test_endpoint_11(self, async_client: AsyncArbi) -> None:
        response = await async_client.api.test.with_raw_response.test_endpoint_11()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        test = await response.parse()
        assert_matches_type(SimpleResponse, test, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_test_endpoint_11(self, async_client: AsyncArbi) -> None:
        async with async_client.api.test.with_streaming_response.test_endpoint_11() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            test = await response.parse()
            assert_matches_type(SimpleResponse, test, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_test_endpoint_12(self, async_client: AsyncArbi) -> None:
        test = await async_client.api.test.test_endpoint_12()
        assert_matches_type(SimpleResponse, test, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_test_endpoint_12(self, async_client: AsyncArbi) -> None:
        response = await async_client.api.test.with_raw_response.test_endpoint_12()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        test = await response.parse()
        assert_matches_type(SimpleResponse, test, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_test_endpoint_12(self, async_client: AsyncArbi) -> None:
        async with async_client.api.test.with_streaming_response.test_endpoint_12() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            test = await response.parse()
            assert_matches_type(SimpleResponse, test, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_test_endpoint_13(self, async_client: AsyncArbi) -> None:
        test = await async_client.api.test.test_endpoint_13()
        assert_matches_type(SimpleResponse, test, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_test_endpoint_13(self, async_client: AsyncArbi) -> None:
        response = await async_client.api.test.with_raw_response.test_endpoint_13()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        test = await response.parse()
        assert_matches_type(SimpleResponse, test, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_test_endpoint_13(self, async_client: AsyncArbi) -> None:
        async with async_client.api.test.with_streaming_response.test_endpoint_13() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            test = await response.parse()
            assert_matches_type(SimpleResponse, test, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_test_endpoint_14(self, async_client: AsyncArbi) -> None:
        test = await async_client.api.test.test_endpoint_14()
        assert_matches_type(SimpleResponse, test, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_test_endpoint_14(self, async_client: AsyncArbi) -> None:
        response = await async_client.api.test.with_raw_response.test_endpoint_14()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        test = await response.parse()
        assert_matches_type(SimpleResponse, test, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_test_endpoint_14(self, async_client: AsyncArbi) -> None:
        async with async_client.api.test.with_streaming_response.test_endpoint_14() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            test = await response.parse()
            assert_matches_type(SimpleResponse, test, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_test_endpoint_15(self, async_client: AsyncArbi) -> None:
        test = await async_client.api.test.test_endpoint_15()
        assert_matches_type(SimpleResponse, test, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_test_endpoint_15(self, async_client: AsyncArbi) -> None:
        response = await async_client.api.test.with_raw_response.test_endpoint_15()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        test = await response.parse()
        assert_matches_type(SimpleResponse, test, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_test_endpoint_15(self, async_client: AsyncArbi) -> None:
        async with async_client.api.test.with_streaming_response.test_endpoint_15() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            test = await response.parse()
            assert_matches_type(SimpleResponse, test, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_test_endpoint_16(self, async_client: AsyncArbi) -> None:
        test = await async_client.api.test.test_endpoint_16()
        assert_matches_type(SimpleResponse, test, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_test_endpoint_16(self, async_client: AsyncArbi) -> None:
        response = await async_client.api.test.with_raw_response.test_endpoint_16()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        test = await response.parse()
        assert_matches_type(SimpleResponse, test, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_test_endpoint_16(self, async_client: AsyncArbi) -> None:
        async with async_client.api.test.with_streaming_response.test_endpoint_16() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            test = await response.parse()
            assert_matches_type(SimpleResponse, test, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_test_endpoint_17(self, async_client: AsyncArbi) -> None:
        test = await async_client.api.test.test_endpoint_17()
        assert_matches_type(SimpleResponse, test, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_test_endpoint_17(self, async_client: AsyncArbi) -> None:
        response = await async_client.api.test.with_raw_response.test_endpoint_17()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        test = await response.parse()
        assert_matches_type(SimpleResponse, test, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_test_endpoint_17(self, async_client: AsyncArbi) -> None:
        async with async_client.api.test.with_streaming_response.test_endpoint_17() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            test = await response.parse()
            assert_matches_type(SimpleResponse, test, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_test_endpoint_18(self, async_client: AsyncArbi) -> None:
        test = await async_client.api.test.test_endpoint_18()
        assert_matches_type(SimpleResponse, test, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_test_endpoint_18(self, async_client: AsyncArbi) -> None:
        response = await async_client.api.test.with_raw_response.test_endpoint_18()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        test = await response.parse()
        assert_matches_type(SimpleResponse, test, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_test_endpoint_18(self, async_client: AsyncArbi) -> None:
        async with async_client.api.test.with_streaming_response.test_endpoint_18() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            test = await response.parse()
            assert_matches_type(SimpleResponse, test, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_test_endpoint_19(self, async_client: AsyncArbi) -> None:
        test = await async_client.api.test.test_endpoint_19()
        assert_matches_type(SimpleResponse, test, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_test_endpoint_19(self, async_client: AsyncArbi) -> None:
        response = await async_client.api.test.with_raw_response.test_endpoint_19()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        test = await response.parse()
        assert_matches_type(SimpleResponse, test, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_test_endpoint_19(self, async_client: AsyncArbi) -> None:
        async with async_client.api.test.with_streaming_response.test_endpoint_19() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            test = await response.parse()
            assert_matches_type(SimpleResponse, test, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_test_endpoint_2(self, async_client: AsyncArbi) -> None:
        test = await async_client.api.test.test_endpoint_2()
        assert_matches_type(SimpleResponse, test, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_test_endpoint_2(self, async_client: AsyncArbi) -> None:
        response = await async_client.api.test.with_raw_response.test_endpoint_2()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        test = await response.parse()
        assert_matches_type(SimpleResponse, test, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_test_endpoint_2(self, async_client: AsyncArbi) -> None:
        async with async_client.api.test.with_streaming_response.test_endpoint_2() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            test = await response.parse()
            assert_matches_type(SimpleResponse, test, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_test_endpoint_20(self, async_client: AsyncArbi) -> None:
        test = await async_client.api.test.test_endpoint_20()
        assert_matches_type(SimpleResponse, test, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_test_endpoint_20(self, async_client: AsyncArbi) -> None:
        response = await async_client.api.test.with_raw_response.test_endpoint_20()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        test = await response.parse()
        assert_matches_type(SimpleResponse, test, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_test_endpoint_20(self, async_client: AsyncArbi) -> None:
        async with async_client.api.test.with_streaming_response.test_endpoint_20() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            test = await response.parse()
            assert_matches_type(SimpleResponse, test, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_test_endpoint_21(self, async_client: AsyncArbi) -> None:
        test = await async_client.api.test.test_endpoint_21()
        assert_matches_type(SimpleResponse, test, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_test_endpoint_21(self, async_client: AsyncArbi) -> None:
        response = await async_client.api.test.with_raw_response.test_endpoint_21()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        test = await response.parse()
        assert_matches_type(SimpleResponse, test, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_test_endpoint_21(self, async_client: AsyncArbi) -> None:
        async with async_client.api.test.with_streaming_response.test_endpoint_21() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            test = await response.parse()
            assert_matches_type(SimpleResponse, test, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_test_endpoint_22(self, async_client: AsyncArbi) -> None:
        test = await async_client.api.test.test_endpoint_22()
        assert_matches_type(SimpleResponse, test, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_test_endpoint_22(self, async_client: AsyncArbi) -> None:
        response = await async_client.api.test.with_raw_response.test_endpoint_22()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        test = await response.parse()
        assert_matches_type(SimpleResponse, test, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_test_endpoint_22(self, async_client: AsyncArbi) -> None:
        async with async_client.api.test.with_streaming_response.test_endpoint_22() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            test = await response.parse()
            assert_matches_type(SimpleResponse, test, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_test_endpoint_23(self, async_client: AsyncArbi) -> None:
        test = await async_client.api.test.test_endpoint_23()
        assert_matches_type(SimpleResponse, test, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_test_endpoint_23(self, async_client: AsyncArbi) -> None:
        response = await async_client.api.test.with_raw_response.test_endpoint_23()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        test = await response.parse()
        assert_matches_type(SimpleResponse, test, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_test_endpoint_23(self, async_client: AsyncArbi) -> None:
        async with async_client.api.test.with_streaming_response.test_endpoint_23() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            test = await response.parse()
            assert_matches_type(SimpleResponse, test, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_test_endpoint_24(self, async_client: AsyncArbi) -> None:
        test = await async_client.api.test.test_endpoint_24()
        assert_matches_type(SimpleResponse, test, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_test_endpoint_24(self, async_client: AsyncArbi) -> None:
        response = await async_client.api.test.with_raw_response.test_endpoint_24()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        test = await response.parse()
        assert_matches_type(SimpleResponse, test, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_test_endpoint_24(self, async_client: AsyncArbi) -> None:
        async with async_client.api.test.with_streaming_response.test_endpoint_24() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            test = await response.parse()
            assert_matches_type(SimpleResponse, test, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_test_endpoint_25(self, async_client: AsyncArbi) -> None:
        test = await async_client.api.test.test_endpoint_25()
        assert_matches_type(SimpleResponse, test, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_test_endpoint_25(self, async_client: AsyncArbi) -> None:
        response = await async_client.api.test.with_raw_response.test_endpoint_25()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        test = await response.parse()
        assert_matches_type(SimpleResponse, test, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_test_endpoint_25(self, async_client: AsyncArbi) -> None:
        async with async_client.api.test.with_streaming_response.test_endpoint_25() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            test = await response.parse()
            assert_matches_type(SimpleResponse, test, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_test_endpoint_26(self, async_client: AsyncArbi) -> None:
        test = await async_client.api.test.test_endpoint_26()
        assert_matches_type(SimpleResponse, test, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_test_endpoint_26(self, async_client: AsyncArbi) -> None:
        response = await async_client.api.test.with_raw_response.test_endpoint_26()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        test = await response.parse()
        assert_matches_type(SimpleResponse, test, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_test_endpoint_26(self, async_client: AsyncArbi) -> None:
        async with async_client.api.test.with_streaming_response.test_endpoint_26() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            test = await response.parse()
            assert_matches_type(SimpleResponse, test, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_test_endpoint_27(self, async_client: AsyncArbi) -> None:
        test = await async_client.api.test.test_endpoint_27()
        assert_matches_type(SimpleResponse, test, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_test_endpoint_27(self, async_client: AsyncArbi) -> None:
        response = await async_client.api.test.with_raw_response.test_endpoint_27()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        test = await response.parse()
        assert_matches_type(SimpleResponse, test, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_test_endpoint_27(self, async_client: AsyncArbi) -> None:
        async with async_client.api.test.with_streaming_response.test_endpoint_27() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            test = await response.parse()
            assert_matches_type(SimpleResponse, test, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_test_endpoint_28(self, async_client: AsyncArbi) -> None:
        test = await async_client.api.test.test_endpoint_28()
        assert_matches_type(SimpleResponse, test, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_test_endpoint_28(self, async_client: AsyncArbi) -> None:
        response = await async_client.api.test.with_raw_response.test_endpoint_28()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        test = await response.parse()
        assert_matches_type(SimpleResponse, test, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_test_endpoint_28(self, async_client: AsyncArbi) -> None:
        async with async_client.api.test.with_streaming_response.test_endpoint_28() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            test = await response.parse()
            assert_matches_type(SimpleResponse, test, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_test_endpoint_29(self, async_client: AsyncArbi) -> None:
        test = await async_client.api.test.test_endpoint_29()
        assert_matches_type(SimpleResponse, test, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_test_endpoint_29(self, async_client: AsyncArbi) -> None:
        response = await async_client.api.test.with_raw_response.test_endpoint_29()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        test = await response.parse()
        assert_matches_type(SimpleResponse, test, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_test_endpoint_29(self, async_client: AsyncArbi) -> None:
        async with async_client.api.test.with_streaming_response.test_endpoint_29() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            test = await response.parse()
            assert_matches_type(SimpleResponse, test, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_test_endpoint_3(self, async_client: AsyncArbi) -> None:
        test = await async_client.api.test.test_endpoint_3()
        assert_matches_type(SimpleResponse, test, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_test_endpoint_3(self, async_client: AsyncArbi) -> None:
        response = await async_client.api.test.with_raw_response.test_endpoint_3()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        test = await response.parse()
        assert_matches_type(SimpleResponse, test, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_test_endpoint_3(self, async_client: AsyncArbi) -> None:
        async with async_client.api.test.with_streaming_response.test_endpoint_3() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            test = await response.parse()
            assert_matches_type(SimpleResponse, test, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_test_endpoint_30(self, async_client: AsyncArbi) -> None:
        test = await async_client.api.test.test_endpoint_30()
        assert_matches_type(SimpleResponse, test, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_test_endpoint_30(self, async_client: AsyncArbi) -> None:
        response = await async_client.api.test.with_raw_response.test_endpoint_30()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        test = await response.parse()
        assert_matches_type(SimpleResponse, test, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_test_endpoint_30(self, async_client: AsyncArbi) -> None:
        async with async_client.api.test.with_streaming_response.test_endpoint_30() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            test = await response.parse()
            assert_matches_type(SimpleResponse, test, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_test_endpoint_4(self, async_client: AsyncArbi) -> None:
        test = await async_client.api.test.test_endpoint_4()
        assert_matches_type(SimpleResponse, test, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_test_endpoint_4(self, async_client: AsyncArbi) -> None:
        response = await async_client.api.test.with_raw_response.test_endpoint_4()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        test = await response.parse()
        assert_matches_type(SimpleResponse, test, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_test_endpoint_4(self, async_client: AsyncArbi) -> None:
        async with async_client.api.test.with_streaming_response.test_endpoint_4() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            test = await response.parse()
            assert_matches_type(SimpleResponse, test, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_test_endpoint_5(self, async_client: AsyncArbi) -> None:
        test = await async_client.api.test.test_endpoint_5()
        assert_matches_type(SimpleResponse, test, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_test_endpoint_5(self, async_client: AsyncArbi) -> None:
        response = await async_client.api.test.with_raw_response.test_endpoint_5()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        test = await response.parse()
        assert_matches_type(SimpleResponse, test, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_test_endpoint_5(self, async_client: AsyncArbi) -> None:
        async with async_client.api.test.with_streaming_response.test_endpoint_5() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            test = await response.parse()
            assert_matches_type(SimpleResponse, test, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_test_endpoint_6(self, async_client: AsyncArbi) -> None:
        test = await async_client.api.test.test_endpoint_6()
        assert_matches_type(SimpleResponse, test, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_test_endpoint_6(self, async_client: AsyncArbi) -> None:
        response = await async_client.api.test.with_raw_response.test_endpoint_6()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        test = await response.parse()
        assert_matches_type(SimpleResponse, test, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_test_endpoint_6(self, async_client: AsyncArbi) -> None:
        async with async_client.api.test.with_streaming_response.test_endpoint_6() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            test = await response.parse()
            assert_matches_type(SimpleResponse, test, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_test_endpoint_7(self, async_client: AsyncArbi) -> None:
        test = await async_client.api.test.test_endpoint_7()
        assert_matches_type(SimpleResponse, test, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_test_endpoint_7(self, async_client: AsyncArbi) -> None:
        response = await async_client.api.test.with_raw_response.test_endpoint_7()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        test = await response.parse()
        assert_matches_type(SimpleResponse, test, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_test_endpoint_7(self, async_client: AsyncArbi) -> None:
        async with async_client.api.test.with_streaming_response.test_endpoint_7() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            test = await response.parse()
            assert_matches_type(SimpleResponse, test, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_test_endpoint_8(self, async_client: AsyncArbi) -> None:
        test = await async_client.api.test.test_endpoint_8()
        assert_matches_type(SimpleResponse, test, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_test_endpoint_8(self, async_client: AsyncArbi) -> None:
        response = await async_client.api.test.with_raw_response.test_endpoint_8()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        test = await response.parse()
        assert_matches_type(SimpleResponse, test, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_test_endpoint_8(self, async_client: AsyncArbi) -> None:
        async with async_client.api.test.with_streaming_response.test_endpoint_8() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            test = await response.parse()
            assert_matches_type(SimpleResponse, test, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_test_endpoint_9(self, async_client: AsyncArbi) -> None:
        test = await async_client.api.test.test_endpoint_9()
        assert_matches_type(SimpleResponse, test, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_test_endpoint_9(self, async_client: AsyncArbi) -> None:
        response = await async_client.api.test.with_raw_response.test_endpoint_9()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        test = await response.parse()
        assert_matches_type(SimpleResponse, test, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_test_endpoint_9(self, async_client: AsyncArbi) -> None:
        async with async_client.api.test.with_streaming_response.test_endpoint_9() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            test = await response.parse()
            assert_matches_type(SimpleResponse, test, path=["response"])

        assert cast(Any, response.is_closed) is True
