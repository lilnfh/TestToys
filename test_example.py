from playwright.sync_api import Page, expect

def test_records_or_updates_the_har_file(page: Page):
    # Get the response from the HAR file
    page.route_from_har("hars/fruit.zip", url="*/**/api/v1/fruits", update=True)

    # Go to the page
    page.goto("https://demo.playwright.dev/api-mocking")

    # Assert that the fruit is visible
    expect(page.get_by_text("Strawberry")).to_be_visible()

"""
# Below, the method is better, we can use it, run in the console. and record our manual operation
# Save API requests from example.com as "example.har" archive.
playwright open --save-har=example.har --save-har-glob="**/itch.io/**" https://itch.io
"""


import re
from playwright.sync_api import Page, expect

def test_has_title(page: Page):
    page.goto("https://playwright.dev/")

    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("Playwright"))

def test_get_started_link(page: Page):
    page.goto("https://playwright.dev/")

    # Click the get started link.
    page.get_by_role("link", name="Get started").click()

    # Expects page to have a heading with the name of Installation.
    expect(page.get_by_role("heading", name="Installation")).to_be_visible()