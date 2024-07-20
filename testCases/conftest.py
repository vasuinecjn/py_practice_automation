import time

import pytest
from seleniumwire import webdriver
from pytest_metadata.plugin import metadata_key


# def pytest_sessionstart(session):
#     # Code to run before any tests are executed
#     print("Starting test session setup")
#
#
# def pytest_sessionfinish(session, exitstatus):
#     # Code to run after all tests have been executed
#     print("Finished test session teardown")


# @pytest.fixture(scope="session", autouse=True)
# def setup_suite():
#     # This fixture will automatically be used for the entire session
#     print("Setup for the entire test suite")
#     yield
#     print("Teardown for the entire test suite")


@pytest.fixture(scope="function")
def setup(request):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('ignore-certificate-errors')
    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.close()
    driver.quit()


def pytest_addoption(parser):  #This will get the value from CLI /hooks
    parser.addoption('--browser')


@pytest.fixture()
def browser(request):  # This will return the Browser value to setup method
    print("request type is ------#####>>>>", type(request))
    return request.config.getoption('--browser')


### pyTest html report ###

# It is hook for adding environment info to HTML Report
def pytest_configure(config):
    config.stash[metadata_key]['Project Name'] = 'nop Commerce'
    config.stash[metadata_key]['Module Name'] = 'Customers'
    config.stash[metadata_key]['Tester'] = 'vasu'


# It is hook for delete/Modify Environment info to HTML Report
@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop('JAVA_HOME', None)
    metadata.pop('Plugins', None)
