from datetime import datetime

from pydantic import BaseModel


class Planet(BaseModel):
    name: str
    rotation_period: str
    orbital_period: str
    diameter: str
    climate: str
    gravity: str
    terrain: str
    surface_water: str
    population: str
    residents: list[str]
    films: list[str]
    created: datetime
    edited: datetime
    url: str

