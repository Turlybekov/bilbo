import allure

from src.helpers.assert_with import assert_with
from src.models.vehicle import Vehicle


@allure.feature("Star wars")
@allure.story("Vehicle")
@allure.title("Check Vehicle list not empty")
def test_get_all_vehicles(all_vehicles):
    vehicle_list = [Vehicle(**vehicle) for vehicle in all_vehicles]
    assert_with(len(vehicle_list) > 0,
                f'Expected specie quantity to be greater than 0, actual: {len(vehicle_list)}')


@allure.feature("Star wars")
@allure.story("Vehicle")
@allure.title("Check Vehicle passengers capacity is 30")
def test_vehicle_passengers_capacity(vehicle_by_id):
    vehicle = Vehicle(**vehicle_by_id(4))
    assert_with(int(vehicle.passengers) == 30,
                f'Expected vehicle passengers capacity to be 30, actual: {vehicle.passengers}')


@allure.feature("Star wars")
@allure.story("Vehicle")
@allure.title("Check Vehicle class")
def test_vehicle_class_type(vehicle_by_id):
    vehicle = Vehicle(**vehicle_by_id(4))
    assert_with(vehicle.vehicle_class == 'wheeled',
                f'Expected vehicle class to be "wheeled" , actual: {vehicle.vehicle_class}')


@allure.feature("Star wars")
@allure.story("Vehicle")
@allure.title("Check Vehicle model")
def test_vehicle_model(vehicle_by_id):
    vehicle = Vehicle(**vehicle_by_id(50))
    assert_with(vehicle.model == 'Low Altitude Assault Transport/infrantry',
                f'Expected vehicle model to be "Low Altitude Assault Transport/infrantry" , actual: {vehicle.model}')
