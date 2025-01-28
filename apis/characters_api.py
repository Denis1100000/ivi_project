from requests import Response
from restclient import Restclient
from .models.characters_model import CharactersResponse, CharacterResponse, CharacterDeletedResponse, Character
from .utilities import validate_status_code, validate_request_json


class CharactersApi:
    def __init__(self, host, auth=None):
        self.host = host
        self.client = Restclient(host=host, auth=auth)

    def get_v2_characters(
            self,
            status_code: int = 200,
            **kwargs
    ) -> Response | CharactersResponse:
        response = self.client.get(
            path="/v2/characters",
            auth=self.client.auth,
            **kwargs
        )
        validate_status_code(response, status_code)
        if response.status_code == 200:
            return CharactersResponse(**response.json())
        return response

    def get_v2_character(
            self,
            name: str,
            status_code: int = 200,
            **kwargs
    ) -> Response | CharacterResponse:
        response = self.client.get(
            path=f"/v2/character?name={'+'.join(name.split())}",
            auth=self.client.auth,
            **kwargs
        )
        validate_status_code(response, status_code)
        if response.status_code == 200:
            return CharacterResponse(**response.json())
        return response

    def post_v2_character(
            self,
            json: Character,
            status_code: int = 200,
            **kwargs
    ) -> Response | CharacterResponse:
        response = self.client.post(
            path="/v2/character",
            auth=self.client.auth,
            json=validate_request_json(json),
            **kwargs
        )
        validate_status_code(response, status_code)
        if response.status_code == 200:
            return CharacterResponse(**response.json())
        return response

    def post_v2_reset(
            self,
            status_code: int,
            **kwargs
    ) -> Response:
        response = self.client.post(
            path="/v2/reset",
            auth=self.client.auth,
            **kwargs
        )
        validate_status_code(response, status_code)
        return response

    def put_v2_character(
            self,
            json: Character,
            status_code: int = 200,
            **kwargs
    ) -> Response | CharacterResponse:
        response = self.client.put(
            path="/v2/character",
            auth=self.client.auth,
            json=validate_request_json(json),
            **kwargs
        )
        validate_status_code(response, status_code)
        if response.status_code == 200:
            return CharacterResponse(**response.json())
        return response

    def delete_v2_character(
            self,
            name: str,
            status_code: int = 200,
            **kwargs
    ) -> Response | CharacterDeletedResponse:
        response = self.client.delete(
            path=f"/v2/character?name={'+'.join(name.split())}",
            auth=self.client.auth,
            **kwargs
        )
        validate_status_code(response, status_code)
        if response.status_code == 200:
            return CharacterDeletedResponse(**response.json())
        return response
