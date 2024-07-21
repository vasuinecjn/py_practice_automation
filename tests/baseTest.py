import pytest
import json
from pathlib import Path


@pytest.mark.usefixtures("init_test")
class BaseTest:

    # @staticmethod
    # def test_case(path):
    #     test_cases = []
    #     with open(path, "r") as f:
    #         data = json.load(f)
    #     for case in data:
    #         if not case["isSkip"]:
    #             test_cases.append(case)
    #     return test_cases

    @classmethod
    def setup_class(cls):
        # Common setup code to run once before all tests in the class
        print(cls.__name__)
