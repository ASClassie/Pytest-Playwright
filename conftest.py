import pytest
from playwright.sync_api import Playwright
import os, json


@pytest.fixture(scope='session')
def browser(playwright: Playwright, request):
    browser_name = request.config.getoption("--browser_name")
    if browser_name == "chrome":
        browser = playwright.chromium.launch(headless=False, args=["--start-maximized"])
    elif browser_name == "firefox":
        browser = playwright.firefox.launch(headless=False, args=["--start-maximized"])
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")
    yield browser
    browser.close()

# this is a also a pytest hook used to add custom command-line options for test execution.
def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome", help="Type in browser name")

@pytest.fixture(scope='function')
def page(browser):
    context = browser.new_context(no_viewport=True)
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    page = context.new_page()
    yield page
    context.tracing.stop(path="test-results/trace.zip")
    context.close()

import pytest
# this is a customer hooks to show the test passed status in command line in different way
def pytest_runtest_logreport(report):
    if report.when == "call":
        if report.failed:
            print(f"\n❌ Test Failed: {report.nodeid}")
        elif report.passed:
            print(f"\n✅ Test Passed: {report.nodeid}")