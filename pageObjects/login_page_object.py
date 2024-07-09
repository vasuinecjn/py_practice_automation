from pageObjects.page_object import Page


class LoginPage(Page):

    def __init__(self, driver):
        super().__init__(driver)

    def set_email(self, email):
        email_element = self.get_element('email_textbox')
        email_element.clear()
        email_element.send_keys(email)

    def set_password(self, password):
        password_element = self.get_element('password_textbox')
        password_element.clear()
        password_element.send_keys(password)

    def click_login(self):
        self.get_element('login_button').click()

    def click_logout(self):
        self.get_element('logout_link').click()
