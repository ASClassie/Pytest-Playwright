import pytest
from playwright.sync_api import Playwright
import os,json

@pytest.fixture(scope='session')
def browser(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False,slow_mo=50)
    yield browser
    browser.close()


@pytest.fixture(scope='function')
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()
