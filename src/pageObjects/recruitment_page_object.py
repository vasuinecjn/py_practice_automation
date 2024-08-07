import time
from logging import Logger

from faker import Faker

from src.constants import TestConstants
from src.pageObjects.page_object import Page
from pathlib import Path

# from src.utilities.stringUtils import get_clean_phone_number
from src.web_operations import WebOperation


class RecruitmentPage(Page):

    def __init__(self, web_op: WebOperation, page_data: dict):
        super().__init__(web_op, page_data)
        self.fake = Faker(['en_US'])

    def select_vacancy(self, vacancy):
        self.web_op.click(self.get_locator("ac_vacancy_dropdown"))
        time.sleep(2)
        self.web_op.click(self.get_locator("ac_vacancy_dropdown_option"), [vacancy])

    def upload_resume(self, resume_path):
        self.web_op.type(self.get_locator("ac_resume_upload_field"), str(Path.cwd().joinpath(resume_path)))

    def consent_to_keep_data(self, consent):
        if consent:
            self.web_op.click(self.get_locator("ac_consent_to_keep_data_checkbox"))

    def add_new_candidate(self, candidate):
        candidate_dict = self.get_page_data(candidate)
        self.web_op.click(self.get_locator("add_candidate_button"))
        self.web_op.type(self.get_locator("ac_first_name"), self.fake.first_name())
        self.web_op.type(self.get_locator("ac_middle_name"), self.fake.first_name())
        self.web_op.type(self.get_locator("ac_last_name"), self.fake.last_name())
        self.select_vacancy(candidate_dict["vacancy"])
        self.web_op.type(self.get_locator("ac_email_textbox"), self.fake.email())
        self.web_op.type(self.get_locator("ac_contact_number_textbox"), "1234567890")
        # self.upload_resume(candidate_dict["resume"])
        self.web_op.type(self.get_locator("ac_keywords_textbox"),
                         ", ".join(self.fake.words(TestConstants.KEYWORDS_LENGTH)))
        # type_in(self.get_element("ac_date_of_application_field"), self.fake.date("%Y-%m-%d"))
        self.web_op.type(self.get_locator("ac_notes_textarea"),
                         " ".join(self.fake.words(TestConstants.NOTES_LENGTH)))
        self.consent_to_keep_data(candidate_dict["consent_to_keep_data"])
        self.web_op.click(self.get_locator("ac_save_button"))
        return self

