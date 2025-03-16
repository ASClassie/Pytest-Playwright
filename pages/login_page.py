
from .base_page import BasePage

class LoginPage(BasePage):

    def __init__(self,page):
        super().__init__(page)
        self.username_field = '#username'
        self.password_field = '#password'
        self.login_button = '#Login'


    def login(self,username:str,password:str):
        self.page.fill(self.username_field,username)
        self.page.fill(self.password_field,password)
        self.page.click(self.login_button)


