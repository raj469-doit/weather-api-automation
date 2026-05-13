import pytest
from api_objects.weather_service import WeatherService
from models.weather_models import WeatherData


def test_get_weather_contract_validation(weather_service):
    """
    Validates that the API response matches our expected data structure (Contract).
    """
    # Act
    response = weather_service.get_current_weather("Oak Point")
    
    # Assert
    assert response.status_code == 200
    
    # This single line validates types, nesting, and presence of all required fields
    try:
        validated_data = WeatherData(**response.json())
        assert validated_data.name == "Oak Point"
    except Exception as e:
        pytest.fail(f"API Contract Violation: {e}")

def test_get_weather_for_invalid_city_returns_404(weather_service):
    """
    Negative test to ensure the API handles non-existent cities correctly.
    """
    response = weather_service.get_current_weather("ThisCityDoesNotExist")
    
    assert response.status_code == 404
    assert response.json()["message"] == "city not found"