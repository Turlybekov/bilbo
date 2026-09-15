import allure
import pytest

from src.helpers.assert_with import assert_with
from src.models.movie import Movie
from tests.data.movie import MOVIE_DATA


@allure.feature("Star wars")
@allure.story("Movie")
@allure.title("Get All Movies")
@allure.testcase("Movie Test")
def test_movie_list_not_empty(all_movies):
    response = [Movie(**movie) for movie in all_movies]
    print(response)
    assert_with(len(response) > 0, 'Movie list is empty')


@allure.feature("Star wars")
@allure.story("Movie")
@allure.title("Check movie names")
@pytest.mark.parametrize('movie_id ,episode_name', MOVIE_DATA)
def test_movie_name(movie_by_id, movie_id, episode_name):
    response = Movie(**movie_by_id(movie_id))
    assert_with(response.title == episode_name, f'Expected movie name: "{episode_name}", actual: "{response.title}"')


@allure.feature("Star wars")
@allure.story("Movie")
@allure.title("Get Movie by ID")
def test_movie_by_id(movie_by_id):
    movie_id = 3
    response = Movie(**movie_by_id(movie_id))
    assert_with(response.episode_id == movie_id,
                f'Expected movie id: "{movie_id}", actual: "{response.episode_id}"')
