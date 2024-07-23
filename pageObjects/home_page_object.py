from pageObjects.page_object import Page


class HomePage(Page):

    def __init__(self, driver):
        super().__init__(driver)

    def logout(self):
        self.click_on('logout_link')
