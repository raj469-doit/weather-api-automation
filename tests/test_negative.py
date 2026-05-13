import pytest
from api_objects.weather_service import WeatherService

def test_unauthorized_access_with_invalid_key():
    # We pass a bogus key to ensure the system handles 401 Unauthorized
    bad_service = WeatherService(api_key="invalid_key_123")
    
    # Update this line to match the actual method name in weather_service.py
    response = bad_service.get_current_weather("London") 
    
    assert response.status_code == 401
    assert "Invalid API key" in response.text