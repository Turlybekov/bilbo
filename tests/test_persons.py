import allure
import pytest

from src.helpers.assert_with import assert_with
from src.models.person import Person
from tests.data.person import PERSON_DATA


@allure.feature("Star wars")
@allure.story("Persons")
@allure.title("Check Person list not empty")
def test_persons_list_not_empty(all_persons):
    persons = [Person(**person) for person in all_persons]
    assert_with(len(persons) > 0, 'Persons list not empty')


@allure.feature("Star wars")
@allure.story("Persons")
@allure.title("Check Person name in list")
def test_person_in_list(all_persons):
    persons_name = [Person(**person).name for person in all_persons]
    assert_with('Watto' in persons_name, 'Watto in persons list')


@allure.feature("Star wars")
@allure.story("Persons")
@allure.title("Check Person name  and birth year")
@pytest.mark.parametrize('person_id, person_name, birth_year', PERSON_DATA)
def test_person_in_list(person_by_id, person_id, person_name, birth_year):
    person = Person(**person_by_id(person_id))
    assert_with(person.name == person_name, f'Expected person name: {person_name}, actual: {person.name}')
    assert_with(person.birth_year == birth_year,
                f'Expected birth year to be: {birth_year}, actual: {person.birth_year}')
