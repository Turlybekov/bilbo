import allure

from src.helpers.assert_with import assert_with
from src.models.specie import Specie


@allure.feature("Star wars")
@allure.story("Species")
@allure.title("Check Species list not empty")
def test_get_all_species(all_species):
    species_list = [Specie(**specie) for specie in all_species]
    assert_with(len(species_list) > 0,
                f'Expected specie quantity to be greater than 0, actual: {len(species_list)}')


@allure.feature("Star wars")
@allure.story("Species")
@allure.title("Check specie classification to be 'reptile")
def test_specie_classification(specie_by_id):
    specie = Specie(**specie_by_id(36))
    assert_with(specie.classification == 'reptile',
                f'Expected specie classification to be "reptile", actual: {specie.classification}')


@allure.feature("Star wars")
@allure.story("Species")
@allure.title("Check specie language to be 'Quermian'")
def test_specie_classification(specie_by_id):
    specie = Specie(**specie_by_id(25))
    assert_with(specie.language == 'Quermian',
                f'Expected specie language to be "Quermian", actual: {specie.classification}')
