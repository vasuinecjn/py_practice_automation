from .baseTest import BaseTest
from .constants import TestConstants


class TestHomePage(BaseTest):

    def test_home_page(self, test_case):
        print("Test Name is ", test_case["testName"])
        self.driver.get(TestConstants.BASE_URL)
