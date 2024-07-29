from src.tests.baseTest import BaseTest


class TestRecruitment(BaseTest):

    def test_add_requirement(self, test_case):
        self.application \
            .go_to_orange_hrm() \
            .login(test_case["login"]) \
            .navigate_to_recruitment_page() \
            .add_new_candidate(test_case["addCandidate"]) \
            .logout()

