from datetime import date, datetime

from pydantic import BaseModel


class Movie(BaseModel):
    title: str
    episode_id: int
    opening_crawl: str
    director: str
    producer: str
    release_date: date
    characters: list[str]
    planets: list[str]
    starships: list[str]
    vehicles: list[str]
    species: list[str]
    created: datetime
    edited: datetime
    url: str
