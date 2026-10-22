import json

import allure

from src.helpers.assert_with import assert_with
from src.models.starship import Starship


@allure.feature("Star wars")
@allure.story("Starships")
@allure.title("Check Starship list not empty")
def test_starships_list_not_empty(all_starships):
    starships = [Starship(**s) for s in all_starships]
    assert_with(len(starships) > 0, f'Expected starship quantity to be greater than 0, actual: {len(starships)}')


@allure.feature("Star wars")
@allure.story("Starships")
@allure.title("Check count of single-crew starships without passengers")
def test_single_crew_starships_count(all_starships):
    expected_quantity = 9
    starships = [
        Starship(**starship)
        for starship in all_starships
        if starship["crew"] == "1" and starship["passengers"] == "0"
    ]
    assert_with(
        len(starships) == expected_quantity,
        "Expected exactly "
        f"{expected_quantity} starships with one crew member and no passengers, "
        f"actual: {len(starships)}",
    )
    starships_json = [starship.model_dump(mode='json') for starship in starships]
    allure.attach(json.dumps(starships_json, indent=2), name='Starships with only 1 crew member and 0 passengers',
                  attachment_type=allure.attachment_type.JSON)
