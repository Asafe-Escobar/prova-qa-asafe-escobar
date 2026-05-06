import pytest
from utils.api_client import ApiClient


@pytest.fixture
def api():
    return ApiClient()
