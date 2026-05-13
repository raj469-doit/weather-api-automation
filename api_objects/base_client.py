import os
import requests
from dotenv import load_dotenv

load_dotenv()

class BaseClient:
    def __init__(self, api_key):
        self.session = requests.Session()
        # We attach the key to the session parameters so every call uses it
        self.session.params = {"appid": api_key}
        self.base_url = "https://api.openweathermap.org/data/2.5"

    def get(self, endpoint, params=None):
        """A generic GET wrapper with error handling."""
        url = f"{self.base_url}/{endpoint}"
        response = self.session.get(url, params=params)
        
        # This will raise an exception for 4xx or 5xx errors
        # useful for debugging later!
        # response.raise_for_status() 
        
        return response