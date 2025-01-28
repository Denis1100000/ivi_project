import pytest
from apis.characters_api import CharactersApi
from helpers import reset_collection
import allure

user = {
    'education': 'Unrevealed',
    'height': 166,
    'identity': 'Business',
    'name': 'Jack',
    'other_aliases': 'Black',
    'universe': 'Marvel',
    'weight': 100.9
}

invalid_user = {
    'education': 'Unrevealed',
    'height': 166,
    'identity': 'Business',
    'name': 'Jack',
    'other_aliases': 'Black',
    'universe': 'Marvel',
    'weight': 100.9
}


@pytest.fixture
def characters_api(request):
    return CharactersApi(
        host=request.config.getoption("--host"),
        auth=(request.config.getoption("--login"), request.config.getoption("--password"))
    )


@allure.step("Подготовка валидного тестового пользователя")
@pytest.fixture
def prepare_user():
    return user


@allure.step("Подготовка невалидного тестового пользователя")
@pytest.fixture
def defected_user():
    return invalid_user


@pytest.fixture(autouse=True)
def reset_after_test(characters_api, request):
    def reset():
        if characters_api.client.auth is not None:
            reset_collection(characters_api)

    request.addfinalizer(reset)


def pytest_addoption(parser):
    parser.addoption("--login", action="store", default="default", help="Login for the tests")
    parser.addoption("--password", action="store", default="default", help="Password for the tests")
    parser.addoption("--host", action="store", default="default", help="Host for the tests")
