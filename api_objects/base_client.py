import os
import requests
from dotenv import load_dotenv

load_dotenv()

class BaseClient:
    def __init__(self):
        self.api_key = os.getenv("OPENWEATHER_API_KEY")
        self.base_url = "https://api.openweathermap.org/data/2.5"
        self.session = requests.Session()
        
        # We add the API key to the session's params so it's 
        # automatically added to every request we make.
        self.session.params = {"appid": self.api_key}

    def get(self, endpoint, params=None):
        """A generic GET wrapper with error handling."""
        url = f"{self.base_url}/{endpoint}"
        response = self.session.get(url, params=params)
        
        # This will raise an exception for 4xx or 5xx errors
        # useful for debugging later!
        # response.raise_for_status() 
        
        return response