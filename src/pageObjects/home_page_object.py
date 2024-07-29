import time

from src.pageObjects.page_object import Page


class HomePage(Page):
    expected = 4

    def __init__(self, driver, test_data):
        super().__init__(driver, test_data)

    def logout(self):
        time.sleep(5)
        # assert self.expected == 5
        self.click_on("user_dropdown")
        self.click_on('logout_link')
