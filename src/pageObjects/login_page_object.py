from logging import Logger

from src.pageObjects.page_object import Page
from src.pageObjects.home_page_object import HomePage
from src.web_operations import WebOperation


class LoginPage(Page):

    def __init__(self, web_op: WebOperation, page_data: dict):
        super().__init__(web_op, page_data)

    def login(self, login):
        login_data = self.get_page_data(login)
        self.web_op.type(self.get_locator("email_textbox"), login_data["userName"])
        self.web_op.type(self.get_locator("password_textbox"), login_data["password"])
        self.web_op.click(self.get_locator("login_button"), "login_button")
        return HomePage(self.web_op, self.page_data)
