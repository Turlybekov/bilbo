from datetime import datetime

from pydantic import BaseModel


class Person(BaseModel):
    name: str
    height: str
    mass: str
    hair_color: str
    skin_color: str
    eye_color: str
    birth_year: str
    gender: str
    homeworld: str
    films: list[str]
    species: list[str]
    vehicles: list[str]
    starships: list[str]
    created: datetime
    edited: datetime
    url: str
