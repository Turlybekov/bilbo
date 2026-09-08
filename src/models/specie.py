from datetime import datetime

from pydantic import BaseModel


class Specie(BaseModel):
    name: str
    classification: str
    designation: str
    average_height: str
    skin_colors: str
    hair_colors: str
    eye_colors: str
    average_lifespan: str
    homeworld: str
    language: str
    people: list[str]
    films: list[str]
    created: datetime
    edited: datetime
    url: str
