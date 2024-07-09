from objectRepository.LoginPageRepository import login_page_elements
from selenium.webdriver.common.by import By


class Page:

    page_locators_map = {
        'LoginPage': login_page_elements
    }

    def __init__(self, driver):
        self.driver = driver

    def get_element(self, key: str):
        locator_type, locator_value = self.get_locator(key).split('|')
        match locator_type:
            case 'id':
                return self.driver.find_element(By.ID, locator_value)
            case 'css_selector':
                return self.driver.find_element(By.CSS_SELECTOR, locator_value)
            case 'link_text':
                return self.driver.find_element(By.LINK_TEXT, locator_value)
            case 'xpath':
                return self.driver.find_element(By.XPATH, locator_value)
            case 'partial_link_text':
                return self.driver.find_element(By.PARTIAL_LINK_TEXT, locator_value)
            case 'name':
                return self.driver.find_element(By.NAME, locator_value)
            case 'class_name':
                return self.driver.find_element(By.CLASS_NAME, locator_value)
            case 'tag_name':
                return self.driver.find_element(By.TAG_NAME, locator_value)
            case _:
                return None

    def get_locator(self, key):
        return self.page_locators_map[self.__class__.__name__][key]

