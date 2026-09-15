import json

import allure
import pytest
from pydantic import BaseModel

from src.clients.movie_client import MovieClient
from src.clients.person_client import PersonClient
from src.clients.planet_client import PlanetClient
from src.clients.specie_client import SpecieClient
from src.clients.starship_client import StarshipClient
from src.clients.vehicle_client import VehicleClient
from src.helpers.assert_with import assert_with


@pytest.fixture(scope="session")
def movie_client():
    client = MovieClient()
    return client


@pytest.fixture(scope="session")
def person_client():
    client = PersonClient()
    return client


@pytest.fixture(scope="session")
def planet_client():
    client = PlanetClient()
    return client


@pytest.fixture(scope="session")
def specie_client():
    client = SpecieClient()
    return client


@pytest.fixture(scope="session")
def starship_client():
    client = StarshipClient()
    return client


@pytest.fixture(scope="session")
def vehicle_client():
    client = VehicleClient()
    return client


@pytest.fixture(scope="session")
def all_movies(movie_client):
    with allure.step("Get all movies"):
        movies = movie_client.get_all_movies()
        assert_with(movies.status_code == 200,
                    f'Expected Response status code is 200, actual: {movies.status_code}')
        json_data = movies.json()
        allure.attach(json.dumps(json_data, indent=2, ensure_ascii=False),
                      name="List of all movies",
                      attachment_type=allure.attachment_type.JSON)
    return json_data


@pytest.fixture(scope="session")
def movie_by_id(movie_client):
    def get_movie(movie_id):
        with allure.step("Get movie by id"):
            movie = movie_client.get_movie_by_id(movie_id)
            assert_with(movie.status_code == 200,
                        f'Expected Response status code is 200, actual: {movie.status_code}')
            json_data = movie.json()
            allure.attach(json.dumps(json_data, indent=2, ensure_ascii=False),
                          name="Received movie by id",
                          attachment_type=allure.attachment_type.JSON)
        return json_data

    return get_movie


@pytest.fixture(scope="session")
def all_persons(person_client):
    with allure.step('Get all persons'):
        persons = person_client.get_all_persons()
        assert_with(persons.status_code == 200,
                    f'Expected Response status code is 200, actual: {persons.status_code}')
        json_data = persons.json()
        allure.attach(json.dumps(json_data, indent=2, ensure_ascii=False),
                      name="List of all persons",
                      attachment_type=allure.attachment_type.JSON)
    return json_data


@pytest.fixture(scope="session")
def person_by_id(person_client):
    def get_person(person_id):
        with allure.step('Get person by id'):
            person = person_client.get_person_by_id(person_id)
            assert_with(person.status_code == 200,
                        f'Expected Response status code is 200, actual: {person.status_code}')
            json_data = person.json()
            allure.attach(json.dumps(json_data, indent=2, ensure_ascii=False),
                          name="Received person by id",
                          attachment_type=allure.attachment_type.JSON)
        return json_data

    return get_person


@pytest.fixture(scope="session")
def all_planets(planet_client):
    with allure.step('Get all planets'):
        planets = planet_client.get_all_planets()
        assert_with(planets.status_code == 200,
                    f'Expected Response status code is 200, actual: {planets.status_code}')
        json_data = planets.json()
        allure.attach(json.dumps(json_data, indent=2, ensure_ascii=False),
                      name="List of all planets",
                      attachment_type=allure.attachment_type.JSON)
    return planets


@pytest.fixture(scope="session")
def planet_by_id(planet_client):
    def get_planet(planet_id):
        with allure.step('Get planet by id'):
            planet = planet_client.get_planet_by_id(planet_id).json()
            assert_with(planet.status_code == 200,
                        f'Expected Response status code is 200, actual: {planet.status_code}')
            json_data = planet.json()
            allure.attach(json.dumps(json_data, indent=2, ensure_ascii=False),
                          name="Received planet by id",
                          attachment_type=allure.attachment_type.JSON)
        return json_data

    return get_planet


@pytest.fixture(scope="session")
def all_species(specie_client):
    with allure.step('Get all species'):
        species = specie_client.get_all_species()
        assert_with(species.status_code == 200,
                    f'Expected Response status code is 200, actual: {species.status_code}')
        json_data = species.json()

        allure.attach(json.dumps(json_data, indent=2, ensure_ascii=False),
                      name="List of all species",
                      attachment_type=allure.attachment_type.JSON)
    return json_data


@pytest.fixture(scope="session")
def specie_by_id(specie_client):
    def get_specie(specie_id):
        with allure.step('Get specie by id'):
            specie = specie_client.get_specie_by_id(specie_id)
            assert_with(specie.status_code == 200,
                        f'Expected Response status code is 200, actual: {specie.status_code}')
            json_data = specie.json()
            allure.attach(json.dumps(json_data, indent=2, ensure_ascii=False),
                          name="Received specie by id",
                          attachment_type=allure.attachment_type.JSON)
        return json_data

    return get_specie


@pytest.fixture(scope="session")
def all_starships(starship_client):
    with allure.step('Get all starships'):
        starships = starship_client.get_all_starships()
        assert_with(starships.status_code == 200,
                    f'Expected Response status code is 200, actual: {starships.status_code}')
        json_data = starships.json()
        allure.attach(json.dumps(json_data, indent=2, ensure_ascii=False),
                      name="List of all starships",
                      attachment_type=allure.attachment_type.JSON)
    return json_data


@pytest.fixture(scope="session")
def starship_by_id(starship_client):
    def get_starship(starship_id):
        with allure.step('Get starship by id'):
            starship = starship_client.get_starship_by_id(starship_id)
            assert_with(starship.status_code == 200,
                        f'Expected Response status code is 200, actual: {starship.status_code}')
            json_data = starship.json()
            allure.attach(json.dumps(json_data, indent=2, ensure_ascii=False),
                          name="Received starship by id",
                          attachment_type=allure.attachment_type.JSON)
        return json_data

    return get_starship


@pytest.fixture(scope="session")
def all_vehicles(vehicle_client):
    with allure.step('Get all vehicles'):
        vehicles = vehicle_client.get_all_vehicles()
        assert_with(vehicles.status_code == 200,
                    f'Expected Response status code is 200, actual: {vehicles.status_code}')
        json_data = vehicles.json()
        allure.attach(json.dumps(json_data, indent=2, ensure_ascii=False),
                      name="List of all vehicles",
                      attachment_type=allure.attachment_type.JSON)
    return json_data


@pytest.fixture(scope="session")
def vehicle_by_id(vehicle_client):
    def get_vehicle(vehicle_id):
        with allure.step('Get vehicle by id'):
            vehicle = vehicle_client.get_vehicle_by_id(vehicle_id)
            assert_with(vehicle.status_code == 200,
                        f'Expected Response status code is 200, actual: {vehicle.status_code}')
            json_data = vehicle.json()
            allure.attach(
                json.dumps(json_data, indent=2, ensure_ascii=False),
                name="Received vehicle by id",
                attachment_type=allure.attachment_type.JSON
            )
            return json_data

    return get_vehicle
