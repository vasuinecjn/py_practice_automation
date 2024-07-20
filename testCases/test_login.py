from utilities.read_properties import Properties
from pageObjects.login_page_object import LoginPage
import inspect
from .constants import TestConstants
from .baseTest import BaseTest


class Test001Login(BaseTest):

    def test_homepage_title(self):
        print('\nnavigating to the base url {0}'.format(TestConstants.BASE_URL))
        self.driver.get(Properties.get_property('baseURL'))
        actual_title = self.driver.title
        if actual_title == 'Your store. Login':
            assert True
        else:
            self.driver.save_screenshot('./Screenshots/' + inspect.stack()[0][3] + '.png')
            assert False

    def test_login(self):
        self.driver.get(TestConstants.BASE_URL)
        self.loginPage = LoginPage(self.driver)
        self.loginPage.set_email(TestConstants.EMAIL)
        self.loginPage.set_password(TestConstants.PASSWORD)
        self.loginPage.click_login()
        actual_title = self.driver.title
        if actual_title == 'Dashboard / nopCommerce administration':
            assert True
        else:
            self.driver.save_screenshot('./Screenshots/' + inspect.stack()[0][3] + '.png')
            assert False
