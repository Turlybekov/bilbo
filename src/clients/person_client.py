import requests

from src.clients.base_client import BaseApiClient


class PersonClient(BaseApiClient):
    PERSON = 'people'
    
    def get_all_persons(self) -> requests.Response:
        response = self.session.get(self._url(self.PERSON))
        return response

    def get_person_by_id(self, person_id) -> requests.Response:
        response = self.session.get(self._url(self.PERSON + f'/{person_id}'))
        return response
