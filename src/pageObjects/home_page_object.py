import time
from logging import Logger

from src.pageObjects.page_object import Page
from src.pageObjects.recruitment_page_object import RecruitmentPage
from src.web_operations import WebOperation


class HomePage(Page):
    expected = 4

    def __init__(self, web_op: WebOperation, page_data: dict):
        super().__init__(web_op, page_data)

    # def logout(self):
    #     time.sleep(5)
    #     # assert self.expected == 5
    #     click_on(self.get_element("user_dropdown"))
    #     click_on(self.get_element("logout_link"))
    #     from src.pageObjects.login_page_object import LoginPage
    #     return LoginPage(self.driver, self.test_data)

    def navigate_to_recruitment_page(self):
        self.web_op.click(self.get_locator("recruitment_link"), "recruitment_link")
        return RecruitmentPage(self.web_op, self.page_data)
