from src.pageObjects.login_page_object import LoginPage
from src.tests.constants import TestConstants


class Application:

    def __init__(self, driver, test_data):
        self.driver = driver
        self.test_data = test_data

    def go_to_orange_hrm(self):
        self.driver.get(TestConstants.BASE_URL)
        return LoginPage(self.driver, self.test_data)
