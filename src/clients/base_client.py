import requests
from src.helpers.settings import settings


class BaseApiClient:

    def __init__(self, base_url: str = settings.base_url, session: requests.Session | None = None):
        self.base_url = base_url
        self.session = session or requests.Session()

    def set_headers(self, headers: dict[str, str]) -> None:
        self.session.headers.update(headers)

    def _url(self, endpoint: str) -> str:
        return f'{self.base_url.rstrip("/")}/{endpoint.lstrip("/")}'

    def post(self, endpoint: str, data: dict, **kwargs) -> requests.Response:
        return self.session.post(url=self._url(endpoint), json=data, **kwargs)

    def put(self, endpoint: str, data: dict, **kwargs) -> requests.Response:
        return self.session.put(url=self._url(endpoint), json=data, **kwargs)

    def patch(self, endpoint: str, data: dict, **kwargs) -> requests.Response:
        return self.session.patch(url=self._url(endpoint), json=data, **kwargs)
