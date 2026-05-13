import os
from api_objects.base_client import BaseClient

class WeatherService(BaseClient):
    def __init__(self, api_key=None):
        # If no key is passed, use the one from the .env file
        api_key = api_key or os.getenv("OPENWEATHER_API_KEY")
        super().__init__(api_key)
        
    def get_current_weather(self, city_name: str):
        """
        Fetches current weather for a specific city.
        Example: weather_service.get_current_weather("London")
        """
        params = {"q": city_name, "units": "metric"}
        return self.get("weather", params=params)

    def get_weather_by_zip(self, zip_code: str, country_code: str = "us"):
        """Fetches weather using ZIP code."""
        params = {"zip": f"{zip_code},{country_code}", "units": "metric"}
        return self.get("weather", params=params)