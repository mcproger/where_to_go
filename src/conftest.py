import pytest

from app.test import TestAPIClient


@pytest.fixture()
def api_client() -> TestAPIClient:
    return TestAPIClient()
