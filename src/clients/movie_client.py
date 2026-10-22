import requests

from src.clients.base_client import BaseApiClient


class MovieClient(BaseApiClient):
    MOVIES = 'films'

    def get_all_movies(self) -> requests.Response:
        return self.get(self.MOVIES)

    def get_movie_by_id(self, movie_id: int) -> requests.Response:
        return self.get(f"{self.MOVIES}/{movie_id}")
