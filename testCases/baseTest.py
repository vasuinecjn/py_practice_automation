import pytest
from utilities.read_properties import Properties


@pytest.fixture()
class BaseTest:
    pass


    # def setup_method(self, method):
    #     # Common setup code to run before each test
    #     self.common_data = "Common setup data"
    #     print(f"Setup for method {method.__name__}")
    #
    # def get_property(self, key):
    #     return self.properties.get_property(key)