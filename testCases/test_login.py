import time

from utilities.read_properties import Properties
from pageObjects.login_page_object import LoginPage
import inspect


class Test001Login:

    def test_homepage_title(self, setup):
        self.driver = setup
        print('\nnavigating to the base url {0}'.format(Properties.get_property('baseURL')))
        self.driver.get(Properties.get_property('baseURL'))
        actual_title = self.driver.title
        if actual_title == 'Your store. Login':
            assert True
        else:
            self.driver.save_screenshot('./Screenshots/' + inspect.stack()[0][3] + '.png')
            assert False

    def test_login(self, setup):
        self.driver = setup
        self.driver.get(Properties.get_property('baseURL'))
        self.loginPage = LoginPage(self.driver)
        self.loginPage.set_email(Properties.get_property('email'))
        self.loginPage.set_password(Properties.get_property('password'))
        self.loginPage.click_login()
        actual_title = self.driver.title
        if actual_title == 'Dashboard / nopCommerce administration':
            assert True
        else:
            self.driver.save_screenshot('./Screenshots/' + inspect.stack()[0][3] + '.png')
            assert False
