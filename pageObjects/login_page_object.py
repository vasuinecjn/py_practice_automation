from pageObjects.page_object import Page
from pageObjects.home_page_object import HomePage


class LoginPage(Page):

    def __init__(self, driver):
        super().__init__(driver)

    def login(self, email, password):
        self.type_in('email_textbox', email)
        self.type_in('password_textbox', password)
        self.click_on('login_button')
        return HomePage(self.driver)
