from pageObjects.page_object import Page
from pageObjects.home_page_object import HomePage


class LoginPage(Page):

    def __init__(self, driver, test_data):
        super().__init__(driver, test_data)

    def login(self, login):
        login_credentials = self.get_data(login)
        self.type_in('email_textbox', login_credentials["userName"])
        self.type_in('password_textbox', login_credentials["password"])
        self.click_on('login_button')
        return HomePage(self.driver, self.test_data)
