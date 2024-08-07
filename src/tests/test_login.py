from src.tests.baseTest import BaseTest


class TestLogin(BaseTest):

    def get_test_file(self):
        return "TestLogin.json"

    def test_login(self, test_case):
        self.get_logger().info("Test Name is " + test_case["testName"])
        self.get_application() \
            .go_to_orange_hrm() \
            .login(test_case["login"]) \
            .logout()
