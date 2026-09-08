import requests

from src.clients.base_client import BaseApiClient


class PlanetClient(BaseApiClient):
    PLANET = 'people'

    def get_all_planets(self) -> requests.Response:
        response = self.session.get(self._url(self.PLANET))
        return response

    def get_planet_by_id(self, planet_id) -> requests.Response:
        response = self.session.get(self._url(self.PLANET + f'/{planet_id}'))
        return response
