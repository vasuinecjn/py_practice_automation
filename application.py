from tests.constants import TestConstants
from pageObjects.login_page_object import LoginPage


class Application:

    def __init__(self, driver):
        self.driver = driver

    def go_to_orange_hrm(self):
        self.driver.get(TestConstants.BASE_URL)
        return LoginPage(self.driver)
