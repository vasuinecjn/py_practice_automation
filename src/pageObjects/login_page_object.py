from src.pageObjects.page_object import Page, click_on, type_in
from src.pageObjects.home_page_object import HomePage


class LoginPage(Page):

    def __init__(self, driver, test_data):
        super().__init__(driver, test_data)

    def login(self, login):
        login_credentials = self.get_data(login)
        type_in(self.get_element("email_textbox"), login_credentials["userName"])
        type_in(self.get_element("password_textbox"), login_credentials["password"])
        click_on(self.get_element("login_button"))
        return HomePage(self.driver, self.test_data)
