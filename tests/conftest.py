import pytest

@pytest.fixture(scope="session")
def base_url():
    # jsonplaceholder base url
    return "https://jsonplaceholder.typicode.com"

@pytest.fixture(scope="session")
def base_url_local():
    # jsonplaceholder base url
    return "http://localhost:5000"
