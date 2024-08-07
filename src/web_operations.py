import os
import time
from logging import Logger
from datetime import datetime
from selenium.common import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from src.utilities.stringUtils import replace_locator_placeholders
from selenium.webdriver.support import expected_conditions as ec


class WebOperation:
    def __init__(self, web_driver, flag_dict, logger: Logger, screenshot_dir, har_dir):
        self.driver = web_driver
        self.flag_dict = flag_dict
        self.logger = logger
        self.screenshot_dir = screenshot_dir
        self.har_dir = har_dir
        self.webDriverWait = WebDriverWait(web_driver,
                                           timeout=10,
                                           poll_frequency=1,
                                           ignored_exceptions=[StaleElementReferenceException, NoSuchElementException])

    def get_driver(self):
        return self.driver

    def get_flag_dict(self):
        return self.flag_dict

    def take_screenshot(self, name):
        self.is_browser_idle()
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        screenshot_path = os.path.join(self.screenshot_dir, f"{timestamp}_{name}.png")
        self.driver.save_screenshot(screenshot_path)

    def get_element(self, locator_by, locator_value):
        def wait_and_get_element(by, value):
            self.is_browser_idle()
            return self.webDriverWait.until(ec.visibility_of_element_located((by, value)))

        match locator_by:
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

    def click(self, locator_tuple, *args):
        locator_key, locator_value = locator_tuple[0], locator_tuple[1]
        if len(args) > 0:
            locator_value = replace_locator_placeholders(locator_value, args[0])
        self.logger.info(f"click on '{locator_key}'")
        by, locator = locator_value.split("|")
        element = self.get_element(by, locator)
        if "yes" == self.flag_dict["click_screenshot"]:
            self.take_screenshot(locator_key)
        element.click()

    def type(self, locator_tuple, text, *args):
        locator_key, locator_value = locator_tuple[0], locator_tuple[1]
        if len(args) > 0:
            locator_value = replace_locator_placeholders(locator_value, args[0])
        self.logger.info(f"type '{text}' in '{locator_key}'")
        by, value = locator_value.split("|")
        element = self.get_element(by, value)
        element.clear()
        element.send_keys(text)

    def is_browser_idle(self, idle_time=2, check_interval=1, wait_time=4):
        return True
        # idle_start_time = time.time()
        #
        # while wait_time > 0:
        #     current_time = time.time()
        #     requests = self.driver.requests
        #     self.logger.info(f"current requests count is {len(requests)}")
        #     if any(request.response is None or request.response.date.timestamp() > (current_time - check_interval) for request in requests):
        #         idle_start_time = current_time
        #
        #     if current_time - idle_start_time >= idle_time:
        #         return True
        #     wait_time -= 1
        #     time.sleep(1)
