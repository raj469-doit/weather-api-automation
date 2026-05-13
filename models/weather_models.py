from pydantic import BaseModel, Field
from typing import List, Optional

class WeatherDescription(BaseModel):
    id: int
    main: str
    description: str
    icon: str

class MainStats(BaseModel):
    temp: float
    feels_like: float
    temp_min: float
    temp_max: float
    pressure: int
    humidity: int

class WeatherData(BaseModel):
    """The 'Contract' for the OpenWeatherMap response."""
    coord: dict
    weather: List[WeatherDescription]
    main: MainStats
    name: str
    cod: int