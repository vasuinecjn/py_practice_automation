from src.pageObjects.login_page_object import LoginPage
from src.constants import TestConstants
from src.web_operations import WebOperation


class Application:

    def __init__(self, web_op: WebOperation, page_data: dict):
        self.web_op = web_op
        self.page_data = page_data

    def go_to_orange_hrm(self):
        self.web_op.get_driver().get(TestConstants.BASE_URL)
        return LoginPage(self.web_op, self.page_data)
