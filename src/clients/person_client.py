import requests

from src.clients.base_client import BaseApiClient


class PersonClient(BaseApiClient):
    PEOPLE = "people"

    def get_all_persons(self) -> requests.Response:
        return self.get(self.PEOPLE)

    def get_person_by_id(self, person_id: int) -> requests.Response:
        return self.get(f"{self.PEOPLE}/{person_id}")
