from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import json
from pathlib import Path


class Page:
    page_locators_map = {}

    def __init__(self, driver, test_data):
        self.driver = driver
        self.test_data = test_data
        self.webDriverWait = WebDriverWait(self.driver, 10)
        locator_file_name = self.__class__.__name__ + ".json"
        locator_file_path = Path(__file__).parent.parent.parent.joinpath("objectRepository").joinpath(locator_file_name)
        if self.__class__.__name__ not in Page.page_locators_map.keys():
            with open(locator_file_path, "r") as f:
                data = json.load(f)
            f.close()
            Page.page_locators_map[self.__class__.__name__] = data

    def get_element(self, key: str):
        locator_type, locator_value = self.get_locator(key)

        def wait_and_get_element(by, lv):
            return self.webDriverWait.until(ec.visibility_of_element_located((by, lv)))

        match locator_type:
            case 'id':
                return wait_and_get_element(By.ID, locator_value)
            case 'css_selector':
                return wait_and_get_element(By.CSS_SELECTOR, locator_value)
            case 'link_text':
                return wait_and_get_element(By.LINK_TEXT, locator_value)
            case 'xpath':
                return wait_and_get_element(By.XPATH, locator_value)
            case 'partial_link_text':
                return wait_and_get_element(By.PARTIAL_LINK_TEXT, locator_value)
            case 'name':
                return wait_and_get_element(By.NAME, locator_value)
            case 'class_name':
                return wait_and_get_element(By.CLASS_NAME, locator_value)
            case 'tag_name':
                return wait_and_get_element(By.TAG_NAME, locator_value)
            case _:
                return None

    def click_on(self, locator: str):
        self.get_element(locator).click()

    def type_in(self, locator: str, value: str):
        element = self.get_element(locator)
        element.clear()
        element.send_keys(value)

    def get_locator(self, key):
        return Page.page_locators_map[self.__class__.__name__][key].split("|")

    def get_data(self, test_data_key):
        return self.test_data[test_data_key]


