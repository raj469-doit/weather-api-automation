import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def driver():
    # Setup Chrome options for Headless mode (required for Codespaces)
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    # Initialize the driver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    yield driver
    
    # Teardown
    driver.quit()

def test_google_weather_search(driver):
    # Navigate to Google
    driver.get("https://www.google.com")
    
    # Simple check to verify we reached the site
    assert "Google" in driver.title
    print("\nSelenium successfully accessed Google in headless mode!")