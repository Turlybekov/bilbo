import requests

from src.clients.base_client import BaseApiClient


class VehicleClient(BaseApiClient):
    VEHICLES = 'vehicles'

    def get_all_vehicles(self) -> requests.Response:
        response = self.session.get(self._url(self.VEHICLES))
        return response

    def get_vehicle_by_id(self, vehicle_id) -> requests.Response:
        response = self.session.get(self._url(self.VEHICLES + f'/{vehicle_id}'))
        return response
