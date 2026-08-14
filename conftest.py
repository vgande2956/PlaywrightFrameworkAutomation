from playwright.sync_api import sync_playwright, Playwright
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


@pytest.fixture(scope="session", autouse=True)
def api_request(playwright:Playwright):
    request = playwright.request.new_context(
        base_url="https://api.restful-api.dev/",
        extra_http_headers={"Content-Type": "application/json", "x-api-key": "2444ef21-be1f-4a38-8a97-0c7ffb2c6c8b"}
    )
    yield request
    request.dispose()