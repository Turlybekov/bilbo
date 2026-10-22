import requests

from src.clients.base_client import BaseApiClient


class SpecieClient(BaseApiClient):
    SPECIES = 'species'

    def get_all_species(self) -> requests.Response:
        return self.get(self.SPECIES)

    def get_specie_by_id(self, specie_id: int) -> requests.Response:
        return self.get(f"{self.SPECIES}/{specie_id}")
