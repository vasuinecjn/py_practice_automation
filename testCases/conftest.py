import pytest
from selenium import webdriver
# from pytest_metadata.plugin import metadata_key


@pytest.fixture(params=["chrome"], scope="function")
def init_test(request):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('ignore-certificate-errors')
    driver = webdriver.Chrome(options=chrome_options)
    request.cls.driver = driver
    yield
    driver.close()
    driver.quit()


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


