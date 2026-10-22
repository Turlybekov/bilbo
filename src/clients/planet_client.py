import requests

from src.clients.base_client import BaseApiClient


class PlanetClient(BaseApiClient):
    PLANETS = "planets"

    def get_all_planets(self) -> requests.Response:
        return self.get(self.PLANETS)

    def get_planet_by_id(self, planet_id: int) -> requests.Response:
        return self.get(f"{self.PLANETS}/{planet_id}")
