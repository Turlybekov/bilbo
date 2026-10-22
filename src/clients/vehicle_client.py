import requests

from src.clients.base_client import BaseApiClient


class VehicleClient(BaseApiClient):
    VEHICLES = 'vehicles'

    def get_all_vehicles(self) -> requests.Response:
        return self.get(self.VEHICLES)

    def get_vehicle_by_id(self, vehicle_id: int) -> requests.Response:
        return self.get(f"{self.VEHICLES}/{vehicle_id}")
