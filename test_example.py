import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.route_from_har("./hars/fruit22.zip", url="*/**/**demo**/**", update=True)
    page.goto("https://demo.playwright.dev/todomvc/")
    page.goto("https://demo.playwright.dev/todomvc/")
    page.goto("https://demo.playwright.dev/todomvc/#/")
    page.screenshot(path="./hars/3.png")
    page.get_by_placeholder("What needs to be done?").click()
    page.screenshot(path="./hars/4.png")
    page.get_by_placeholder("What needs to be done?").fill("aaaabbbbccc")
    page.screenshot(path="./hars/5.png")
    page.get_by_text("Part of TodoMVC").click()
    page.screenshot(path="./hars/6.png")

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
