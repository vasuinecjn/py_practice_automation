import time

import json
from logging import Logger
from pathlib import Path
from src.web_operations import WebOperation


class Page:
    page_locators_dict = {}

    def __init__(self, web_op: WebOperation, page_data: dict):
        self.web_op = web_op
        self.page_data = page_data
        locator_file_name = self.__class__.__name__ + ".json"
        locator_file_path = Path(__file__).parent.parent.parent.joinpath("objectRepository").joinpath(locator_file_name)
        if self.__class__.__name__ not in Page.page_locators_dict.keys():
            with open(locator_file_path, "r") as f:
                data = json.load(f)
            f.close()
            Page.page_locators_dict[self.__class__.__name__] = data

    def get_locator(self, key: str):
        locator = Page.page_locators_dict[self.__class__.__name__][key]
        # if len(args) > 0:
        #     locator = replace_locator_placeholders(locator, args[0])
        return tuple([key, locator])

    def get_page_data(self, key):
        return self.page_data[key]

    def logout(self):
        time.sleep(5)
        self.web_op.click(self.get_locator("user_dropdown"))
        self.web_op.click(self.get_locator("logout_link"))


