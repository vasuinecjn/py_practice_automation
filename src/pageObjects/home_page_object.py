import time
from src.pageObjects.page_object import Page, click_on, type_in
from src.pageObjects.recruitment_page_object import RecruitmentPage


class HomePage(Page):
    expected = 4

    def __init__(self, driver, test_data):
        super().__init__(driver, test_data)

    # def logout(self):
    #     time.sleep(5)
    #     # assert self.expected == 5
    #     click_on(self.get_element("user_dropdown"))
    #     click_on(self.get_element("logout_link"))
    #     from src.pageObjects.login_page_object import LoginPage
    #     return LoginPage(self.driver, self.test_data)

    def navigate_to_recruitment_page(self):
        click_on(self.get_element("recruitment_link"))
        return RecruitmentPage(self.driver, self.test_data)
