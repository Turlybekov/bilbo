import requests

from src.clients.base_client import BaseApiClient


class StarshipClient(BaseApiClient):
    STARSHIPS = 'starships'

    def get_all_starships(self) -> requests.Response:
        return self.get(self.STARSHIPS)

    def get_starship_by_id(self, starship_id: int) -> requests.Response:
        return self.get(f"{self.STARSHIPS}/{starship_id}")
