import pytest


@pytest.mark.usefixtures("init_test")
class BaseTest:

    @classmethod
    def setup_class(cls):
        # Common setup code to run once before all tests in the class
        print(cls.__name__)
