from .baseTest import BaseTest
from src.constants import TestConstants


class TestHomePage(BaseTest):

    def get_test_file(self):
        return "TestHomePage.json"

    def test_home_page(self, test_case):
        self.get_logger().info("Test Name is " + test_case["testName"])
        self.get_application().web_op.get_driver().get(TestConstants.BASE_URL)
