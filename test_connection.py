import requests
import os
from dotenv import load_dotenv

load_dotenv()

def test_api_is_reachable():
    api_key = os.getenv("OPENWEATHER_API_KEY")
    
    # Debugging prints
    if api_key is None:
        print("\n❌ ERROR: API Key is None. Check your .env file!")
    else:
        # Only print the first 4 characters for security
        print(f"\nFound key: {api_key[:4]}****")

    url = f"https://api.openweathermap.org/data/2.5/weather?q=London&appid={api_key}"
    response = requests.get(url)
    
    # Printing the server's specific reason for failure
    if response.status_code != 200:
        print(f"Server Message: {response.json().get('message')}")
        
    assert response.status_code == 200