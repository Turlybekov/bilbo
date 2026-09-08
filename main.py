# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import requests

from src.clients.movie_client import MovieClient
from src.helpers.settings import settings
from src.models.movie import Movie


def fetch_swapi_data():
    url = f"https://swapi.info/api/"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        print(data)
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    fetch_swapi_data()
    print(f'Printing ENV file Base URL: {settings.base_url}')
    movie = MovieClient()
    all_movies = movie.get_all_movies()
    for movie in all_movies:
        if movie.release_date.year < 1980:
            print(movie)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
