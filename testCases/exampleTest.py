from .baseTest import BaseTest


class TestExample(BaseTest):

    def test_one(self):
        assert self.common_data == "Common setup data"
        print("Running test_one")

    def test_two(self):
        assert self.common_data == "Common setup data"
        print("Running test_two")
