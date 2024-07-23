from src.pageObjects.page_object import Page


class HomePage(Page):

    def __init__(self, driver, test_data):
        super().__init__(driver, test_data)

    def logout(self):
        self.click_on("user_dropdown")
        self.click_on('logout_link')
