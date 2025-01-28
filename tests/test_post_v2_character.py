from helpers import create_new_character, get_characters_list, generate_random_user
import allure


@allure.severity(allure.severity_level.NORMAL)
@allure.title("Проверка создания персонажа")
def test_post_v2_character(characters_api, prepare_user):
    new_character = create_new_character(characters_api, prepare_user, status_code=200)
    assert new_character.result.name == prepare_user['name']


@allure.severity(allure.severity_level.NORMAL)
@allure.title("Проверка заполнения базы, ограничение в 500 персонажей")
def test_post_many_characters(characters_api, prepare_user):
    characters_collection = 500 - len(get_characters_list(characters_api))
    for i in range(characters_collection):
        create_new_character(characters_api, generate_random_user(), status_code=200)
    response = create_new_character(characters_api, prepare_user, status_code=400)
    assert response.json()['error'] == "Collection can't contain more than 500 items"


@allure.severity(allure.severity_level.NORMAL)
@allure.title("Проверка на пропуск и неправильный тип данных при создании персонажа")
def test_post_missing_data_request(characters_api, defected_user):
    del defected_user['name']
    defected_user['weight'] = "hello"
    invalid_user = create_new_character(characters_api, defected_user, status_code=400)
    assert invalid_user.json()['error'] == "name: ['Missing data for required field.'], weight: ['Not a valid number.']"


@allure.severity(allure.severity_level.NORMAL)
@allure.title("Проверка на авторизацию для метода POST /v2/character")
def test_post_character_without_auth(characters_api, prepare_user):
    characters_api.client.auth = None
    response = characters_api.post_v2_character(status_code=401, json={})
    assert response.json()['error'] == 'You have to login with proper credentials'
