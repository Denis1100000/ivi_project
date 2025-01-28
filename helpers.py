import string
import random
from faker import Faker


def get_characters_list(characters_api):
    return characters_api.get_v2_characters().result


def get_character_from_list(characters_api, status_code: int):
    characters_response = characters_api.get_v2_character(status_code=status_code)
    return characters_response


def get_random_character_from_list(characters_api, status_code: int):
    characters_response = characters_api.get_v2_characters(status_code=status_code)
    return characters_response.result[random.randint(0, len(characters_response.result) - 1)].name


def generate_random_string(lenght, num: bool = False):
    if num:
        letters = string.ascii_letters + string.digits
    else:
        letters = string.ascii_letters
    return ''.join(random.choice(letters) for _ in range(lenght)).lower()


def create_new_character(characters_api, prepare_user: dict, status_code: int):
    response = characters_api.post_v2_character(json=prepare_user, status_code=status_code)
    return response


def reset_collection(characters_api):
    response = characters_api.post_v2_reset(status_code=200)
    return response


def generate_random_user():
    fake = Faker()
    user = {
        'education': fake.text(max_nb_chars=100),
        'height': random.randint(100, 200),
        'identity': fake.text(max_nb_chars=100),
        'name': fake.text(max_nb_chars=100),
        'other_aliases': fake.text(max_nb_chars=100),
        'universe': fake.text(max_nb_chars=100),
        'weight': round(random.uniform(50.0, 150.0), 2)
    }
    return user


def edit_character(characters_api, update_character: dict):
    return characters_api.put_v2_character(json=update_character).result


def delete_character_by_name(characters_api, character_name: str, status_code: int):
    return characters_api.delete_v2_character(name=character_name, status_code=status_code)
