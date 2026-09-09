import allure

from src.helpers.asssert_with import assert_with
from src.models.person import Person


@allure.feature("Star wars")
@allure.story("Persons")
@allure.title("Get all persons")
@allure.testcase("Check Person list not empty")
def test_persons_list_not_empty(all_persons):
    persons = [Person(**person) for person in all_persons]
    assert_with(len(persons) > 0, 'Persons list not empty')


@allure.feature("Star wars")
@allure.story("Persons")
@allure.title("Get all persons")
@allure.testcase("Check Person name in list")
def test_person_in_list(all_persons):
    persons_name = [Person(**person).name for person in all_persons]
    assert_with('Watto' in persons_name, 'Watto in persons list')
