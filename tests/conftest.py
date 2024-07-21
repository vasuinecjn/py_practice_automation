import pytest
from selenium import webdriver
# from pytest_metadata.plugin import metadata_key
import json
from pathlib import Path


@pytest.fixture(params=["chrome"], scope="function")
def init_test(request):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('ignore-certificate-errors')
    driver = webdriver.Chrome(options=chrome_options)
    request.cls.driver = driver
    yield
    driver.close()
    driver.quit()


def pytest_generate_tests(metafunc):
    test_cases = []
    file_name = metafunc.cls.__name__ + ".json"
    test_cases_file_path = Path(__file__).parent.parent.joinpath("test_cases").joinpath(file_name)
    if "test_case" in metafunc.fixturenames:
        with open(test_cases_file_path, "r") as f:
            data = json.load(f)
        for case in data:
            if not case["isSkip"]:
                test_cases.append(case)
        metafunc.parametrize("test_case", test_cases)

# @pytest.fixture
# def test_cases(request):
#     # Extract the parameter value
#     test_case_file = request.param
#     test_cases = []
#     with open(test_case_file, "r") as f:
#         data = json.load(f)
#     for case in data:
#         if not case["isSkip"]:
#             test_cases.append(case)
#     return test_cases
#


# def pytest_addoption(parser):  #This will get the value from CLI /hooks
#     parser.addoption('--browser')
#
#
# @pytest.fixture()
# def browser(request):  # This will return the Browser value to setup method
#     return request.config.getoption('--browser')


### pyTest html report ###

# It is hook for adding environment info to HTML Report
# def pytest_configure(config):
#     config.stash[metadata_key]['Project Name'] = 'nop Commerce'
#     config.stash[metadata_key]['Module Name'] = 'Customers'
#     config.stash[metadata_key]['Tester'] = 'Sjn'


# It is hook for delete/Modify Environment info to HTML Report
# @pytest.hookimpl(optionalhook=True)
# def pytest_metadata(metadata):
#     metadata.pop('JAVA_HOME', None)
#     metadata.pop('Plugins', None)


