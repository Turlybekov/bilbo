import json

import allure
import pytest

from src.helpers.asssert_with import assert_with
from src.models.starship import Starship


@allure.feature("Star wars")
@allure.story("Starships")
@allure.title("Get all starships")
@allure.testcase("Check Starship list not empty")
def test_starships_list_not_empty(all_starships):
    starships = [Starship(**s) for s in all_starships]
    assert_with(len(starships) > 0, f'Expected starship quantity to be greater than 0, actual: {len(starships)}')


@allure.feature("Star wars")
@allure.story("Starships")
@allure.title("Get all starship with single crew member and 0 passengers")
@allure.testcase(f"Check starship with single crew member and 0 passengers quantity more than n")
@pytest.mark.parametrize('starship_quantity', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
def test_starships_with_single_crew(all_starships, starship_quantity):
    starships = [Starship(**s) for s in all_starships if Starship(**s).crew == '1' and Starship(**s).passengers == '0']
    assert_with(len(starships) >= starship_quantity,
                f'Expected starships with only 1 crew members and no passengers is equal or more than: {starship_quantity}, actual: {len(starships)}')
    starships_json = [starship.model_dump(mode='json') for starship in starships]
    allure.attach(json.dumps(starships_json, indent=2), name='Starships with only 1 crew member and 0 passengers',
                  attachment_type=allure.attachment_type.JSON)
