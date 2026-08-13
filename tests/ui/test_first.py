def test_example_one(page):
    page.goto("https://www.google.com")
    assert page.title() == "Google"
    print("Test passed: Page title is 'Google'")