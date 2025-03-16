from playwright.sync_api import Page
import random

# Utility functions help with reusable code like interacting with elements or validation.

def generate_random_email():
    return f"user{random.randint(1000, 9999)}@example.com"


def take_screenshot(page: Page, name):
    page.screenshot(path=f'/screenshots/{name}.png')
