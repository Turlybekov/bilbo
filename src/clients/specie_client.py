import requests

from src.clients.base_client import BaseApiClient


class SpecieClient(BaseApiClient):
    SPECIES = 'species'

    def get_all_species(self) -> requests.Response:
        response = self.session.get(self._url(self.SPECIES))
        return response

    def get_specie_by_id(self, specie_id) -> requests.Response:
        response = self.session.get(self._url(self.SPECIES + f'/{specie_id}'))
        return response
