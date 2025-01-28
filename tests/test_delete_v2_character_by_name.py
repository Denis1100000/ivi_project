from helpers import create_new_character, delete_character_by_name
import allure


@allure.severity(allure.severity_level.NORMAL)
@allure.title("Проверка удаления созданного персонажа")
def test_delete_v2_character_by_name(characters_api, prepare_user):
    with allure.step("Создание нового персонажа"):
        new_character = create_new_character(characters_api, prepare_user, status_code=200)
        assert new_character.result.name == prepare_user['name']
    with allure.step("Удаление созданного персонажа"):
        deleted_character = delete_character_by_name(characters_api, new_character.result.name, status_code=200)
        assert deleted_character.result == f'Hero {new_character.result.name} is deleted'


@allure.severity(allure.severity_level.NORMAL)
@allure.title("Проверка удаления неизвестного персонажа")
def test_delete_v2_unknown_character_name(characters_api):
    character_name = 'Hello World!'
    response = delete_character_by_name(characters_api, character_name, status_code=400)
    assert response.json()['error'] == 'No such name'


@allure.severity(allure.severity_level.NORMAL)
@allure.title("Проверка на авторизацию для метода DELETE /v2/character")
def test_delete_v2_character_without_auth(characters_api):
    characters_api.client.auth = None
    char_name = 'Test'
    response = delete_character_by_name(characters_api, char_name, status_code=401)
    assert response.json()['error'] == 'You have to login with proper credentials'
