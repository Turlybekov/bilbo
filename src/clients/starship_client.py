import requests

from src.clients.base_client import BaseApiClient


class StarshipClient(BaseApiClient):
    STARSHIPS = 'starships'

    def get_all_starships(self) -> requests.Response:
        response = self.session.get(self._url(self.STARSHIPS))
        return response

    def get_starship_by_id(self, starship_id) -> requests.Response:
        response = self.session.get(self._url(self.STARSHIPS + f'/{starship_id}'))
        return response
