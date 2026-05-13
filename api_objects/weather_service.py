from api_objects.base_client import BaseClient

class WeatherService(BaseClient):
    def __init__(self):
        # Initialize the BaseClient (sets up session, base_url, and api_key)
        super().__init__()

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