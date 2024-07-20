from utilities.read_properties import Properties
from pageObjects.login_page_object import LoginPage
import inspect
from .baseTest import BaseTest


class Test001Login(BaseTest):

    def test_homepage_title(self, setup):
        self.driver = setup
        print('\nnavigating to the base url {0}'.format("https://admin-demo.nopcommerce.com/"))
        self.driver.get("https://admin-demo.nopcommerce.com/")
        actual_title = self.driver.title
        if actual_title == 'Your store. Login':
            assert True
        else:
            self.driver.save_screenshot('./Screenshots/' + inspect.stack()[0][3] + '.png')
            assert False

    def test_login(self, setup):
        self.driver = setup
        self.driver.get("https://admin-demo.nopcommerce.com/")
        self.loginPage = LoginPage(self.driver)
        self.loginPage.set_email("admin@yourstore.com")
        self.loginPage.set_password("admin")
        self.loginPage.click_login()
        actual_title = self.driver.title
        if actual_title == 'Dashboard / nopCommerce administration':
            assert True
        else:
            self.driver.save_screenshot('./Screenshots/' + inspect.stack()[0][3] + '.png')
            assert False
