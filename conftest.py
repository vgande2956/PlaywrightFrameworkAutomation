from playwright.sync_api import sync_playwright
import pytest

@pytest.fixture(scope="session")
def browser(playwright):
    browser = playwright.chromium.launch(headless=False)
    yield browser
    browser.close()
    
def page(browser):
    page = browser.new_page()
    yield page
    page.close()