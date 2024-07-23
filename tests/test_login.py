from .constants import TestConstants
from .baseTest import BaseTest


class TestLogin(BaseTest):

    def test_login(self, test_case):
        self.application\
            .go_to_orange_hrm()\
            .login(TestConstants.EMAIL, TestConstants.PASSWORD)\
            .logout()
