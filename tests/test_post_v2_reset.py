from helpers import reset_collection
from conftest import characters_api
import allure


@allure.severity(allure.severity_level.NORMAL)
@allure.title("Проверка на успешный сброс коллекции")
def test_post_v2_reset(characters_api):
    response = reset_collection(characters_api)
    assert response.status_code == 200


@allure.severity(allure.severity_level.NORMAL)
@allure.title("Проверка на авторизацию для метода POST /v2/reset")
def test_post_v2_reset_without_auth(characters_api):
    characters_api.client.auth = None
    response = characters_api.post_v2_reset(status_code=401)
    assert response.json()['error'] == 'You have to login with proper credentials'
