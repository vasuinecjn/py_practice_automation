import time

from faker import Faker

from src.constants import TestConstants
from src.pageObjects.page_object import Page, click_on, type_in
from pathlib import Path

from src.utilities.stringUtils import get_clean_phone_number


class RecruitmentPage(Page):

    def __init__(self, driver, test_data):
        super().__init__(driver, test_data)
        self.fake = Faker(['en_US'])

    def select_vacancy(self, vacancy):
        print(vacancy)
        click_on(self.get_element("ac_vacancy_dropdown"))
        time.sleep(2)
        click_on(self.get_element("ac_vacancy_dropdown_option", vacancy))

    def upload_resume(self, resume_path):
        type_in(self.get_element("ac_resume_upload_field"), str(Path.cwd().joinpath(resume_path)))

    def consent_to_keep_data(self, consent):
        if consent == True:
            click_on(self.get_element("ac_consent_to_keep_data_checkbox"))

    def add_new_candidate(self, candidate):
        candidate_dict = self.get_data(candidate)
        click_on(self.get_element("add_candidate_button"))
        type_in(self.get_element("ac_first_name"), self.fake.first_name())
        type_in(self.get_element("ac_middle_name"), self.fake.first_name())
        type_in(self.get_element("ac_last_name"), self.fake.last_name())
        self.select_vacancy([candidate_dict["vacancy"]])
        type_in(self.get_element("ac_email_textbox"), self.fake.email())
        type_in(self.get_element("ac_contact_number_textbox"), "1234567890")
        # self.upload_resume(candidate_dict["resume"])
        type_in(self.get_element("ac_keywords_textbox"), ", ".join(self.fake.words(TestConstants.KEYWORDS_LENGTH)))
        # type_in(self.get_element("ac_date_of_application_field"), self.fake.date("%Y-%m-%d"))
        type_in(self.get_element("ac_notes_textarea"), " ".join(self.fake.words(TestConstants.NOTES_LENGTH)))
        self.consent_to_keep_data(candidate_dict["consent_to_keep_data"])
        click_on(self.get_element("ac_save_button"))
        return self

