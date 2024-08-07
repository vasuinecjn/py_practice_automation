import pytest
from abc import ABC, abstractmethod


@pytest.mark.usefixtures("init_test")
class BaseTest(ABC):

    @abstractmethod
    def get_test_file(self):
        pass

    @classmethod
    def setup_class(cls):
        # Common setup code to run once before all tests in the class
        print(cls.__name__)

    def get_logger(self):
        return self.application.web_op.logger

    def get_web_op(self):
        return self.application.web_op

    def get_application(self):
        return self.application