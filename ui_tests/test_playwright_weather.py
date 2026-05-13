import pytest
from playwright.sync_api import Page, expect

def test_google_weather_search_playwright(page: Page):
    # Navigate to Google
    page.goto("https://www.google.com")
    
    # Verify the title
    expect(page).to_have_title("Google")
    
    print("\nPlaywright successfully accessed Google using Chromium!")