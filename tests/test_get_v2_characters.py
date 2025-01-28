from helpers import get_characters_list
import allure


@allure.severity(allure.severity_level.NORMAL)
@allure.title("Проверка получения списка персонажей")
def test_get_characters(characters_api):
    assert len(get_characters_list(characters_api)) == 302


@allure.severity(allure.severity_level.NORMAL)
@allure.title("Проверка на авторизацию для метода GET /v2/characters")
def test_get_v2_character_without_auth(characters_api):
    characters_api.client.auth = None
    response = characters_api.get_v2_characters(status_code=401)
    assert response.json()['error'] == 'You have to login with proper credentials'
