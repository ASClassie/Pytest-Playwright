from xml.dom import VALIDATION_ERR

import pytest
from pages.login_page import LoginPage
from playwright.sync_api import expect
import json, os

VALIDATION_ERR = "Please check your username and password. If you still can't log in, contact your Salesforce administrator."
def user_data():
    file_path = os.path.join(os.path.dirname(__file__), '../Data/users.json')
    with open(file_path, 'r') as file:
        return json.load(file)

@pytest.fixture
def valid_user():
    users = user_data()
    return users[0]


def invalid_user():
    users = user_data()
    return users[1:]


class TestLogin:

    def test_successfull_login(self, page, valid_user):
        login_page = LoginPage(page)
        login_page.navigate('https://qainfotech5-dev-ed.my.salesforce.com/')
        login_page.login(valid_user['username'], valid_user['password'])
        print(page.url)

    @pytest.mark.parametrize("users", invalid_user())
    def test_invalid_login(self, page, users):
        login_page = LoginPage(page)
        login_page.navigate('https://qainfotech5-dev-ed.my.salesforce.com/')
        login_page.login(users['username'], users['password'])
        expect(page.locator('#error')).to_have_text(VALIDATION_ERR)
        # assert VALIDATION_ERR in page.inner_text('#error')
