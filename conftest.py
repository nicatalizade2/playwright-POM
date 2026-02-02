import pytest
import yaml
from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage

with open('config.yaml', 'r') as file:
    config = yaml.safe_load(file)

@pytest.fixture
def page():
    with sync_playwright() as p:
        browser = p[config["browser"]].launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        # Open base_url from config
        page.goto(config["base_url"])

        yield page
        browser.close()

@pytest.fixture
def login_page(page):
    return LoginPage(page)