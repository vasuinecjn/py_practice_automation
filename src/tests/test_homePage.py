from .baseTest import BaseTest
from src.constants import TestConstants


class TestHomePage(BaseTest):

    def test_home_page(self, test_case):
        print("Test Name is ", test_case["testName"])
        self.web_op.get_driver().get(TestConstants.BASE_URL)
