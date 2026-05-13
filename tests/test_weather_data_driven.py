import pytest

@pytest.mark.parametrize("city, expected_country", [
    ("London", "GB"),
    ("Tokyo", "JP"),
    ("Oak Point", "US")
])
def test_multiple_cities(weather_service, city, expected_country):
    response = weather_service.get_current_weather(city)
    assert response.status_code == 200
    assert response.json()["sys"]["country"] == expected_country