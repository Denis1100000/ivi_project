from helpers import edit_character, create_new_character
import allure


@allure.severity(allure.severity_level.NORMAL)
@allure.title("Проверка на изменение созданного персонажа")
def test_put_character(characters_api, prepare_user):
    new_character = create_new_character(characters_api, prepare_user, status_code=200)
    assert new_character.result.name == prepare_user['name']

    update_character = {
        'education': 'Graduate',
        'height': 170,
        'identity': 'Entrepreneur',
        'name': 'Jack',
        'universe': 'Marvel',
        'weight': 85.5
    }

    edited_character = edit_character(characters_api, update_character)
    assert edited_character.education == update_character.get('education')
    assert edited_character.height == update_character.get('height')
    assert edited_character.identity == update_character.get('identity')
    assert edited_character.name == update_character.get('name')
    assert edited_character.universe == update_character.get('universe')
    assert edited_character.weight == update_character.get('weight')


@allure.severity(allure.severity_level.NORMAL)
@allure.title("Проверка на авторизацию для метода PUT /v2/character")
def test_put_character_without_auth(characters_api, prepare_user):
    characters_api.client.auth = None
    response = characters_api.put_v2_character(status_code=401, json={})
    assert response.json()['error'] == 'You have to login with proper credentials'
