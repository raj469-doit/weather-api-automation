import pytest
from api_objects.weather_service import WeatherService

@pytest.fixture
def weather_service():
    """This fixture is now shared with all test files."""
    return WeatherService()