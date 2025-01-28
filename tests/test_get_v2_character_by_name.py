from helpers import get_random_character_from_list, generate_random_string
import random
import pytest
import allure


@allure.severity(allure.severity_level.NORMAL)
@allure.title("Проверка поиска персонажа")
def test_get_v2_character_by_name(characters_api):
    name = 'Avalanche'
    response = characters_api.get_v2_character(name=name, status_code=200)
    assert response.result.name == name


@allure.severity(allure.severity_level.NORMAL)
@allure.title("Проверка поиска персонажа по рандомному имени")
def test_get_v2_character_by_random_name(characters_api):
    name = get_random_character_from_list(characters_api, status_code=200)
    response = characters_api.get_v2_character(name=name, status_code=200)


@pytest.mark.parametrize('name', [
    (
            str(generate_random_string(random.randint(5, 10), num=True))
    )])
@allure.severity(allure.severity_level.NORMAL)
@allure.title("Проверка поиска персонажа по несуществующему имени")
def test_get_v2_unknown_character_name(characters_api, name):
    response = characters_api.get_v2_character(name=name, status_code=400)
    assert response.json()['error'] == 'No such name'


@allure.severity(allure.severity_level.NORMAL)
@allure.title("Проверка на авторизацию для метода GET /v2/character")
def test_get_v2_character_without_auth(characters_api):
    characters_api.client.auth = None
    char_name = 'Jack'
    response = characters_api.get_v2_character(name=char_name, status_code=401)
    assert response.json()['error'] == 'You have to login with proper credentials'
