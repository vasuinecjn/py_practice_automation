from src.tests.baseTest import BaseTest


class TestLogin(BaseTest):

    def test_login(self, test_case):
        self.application \
            .go_to_orange_hrm() \
            .login(test_case["login"]) \
            .logout()
