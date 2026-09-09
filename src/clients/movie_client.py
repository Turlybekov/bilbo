import requests

from src.clients.base_client import BaseApiClient


class MovieClient(BaseApiClient):
    MOVIES = 'films'

    def get_all_movies(self) -> requests.Response:
        response = self.session.get(self._url(self.MOVIES))
        return response

    def get_movie_by_id(self, movie_id) -> requests.Response:
        response = self.session.get(self._url(self.MOVIES + f'/{movie_id}'))
        return response
