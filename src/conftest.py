from src.application import Application
import settings
import pytest
import pytest_html
from selenium import webdriver
import json
from pathlib import Path
import re

driver = None


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default=settings.browser)


def load_test_data():
    test_data_map = {}
    data_path = Path.cwd().joinpath("test_data").joinpath("testData.json")
    with open(data_path, "r") as f:
        data = json.load(f)
    f.close()
    for k in data.keys():
        for ki, v in data[k].items():
            test_data_map[ki] = v
    return test_data_map


@pytest.fixture
def get_browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="function")
def init_test(request, get_browser):
    global driver
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('ignore-certificate-errors')
    driver = webdriver.Chrome(options=chrome_options)
    request.cls.driver = driver
    request.cls.application = Application(driver, load_test_data())
    yield
    driver.close()
    driver.quit()


def pytest_generate_tests(metafunc):
    test_cases = []
    file_name = metafunc.cls.__name__ + ".json"
    test_cases_file_path = Path.cwd().joinpath("test_cases").joinpath(file_name)
    if "test_case" in metafunc.fixturenames:
        with open(test_cases_file_path, "r") as f:
            data = json.load(f)
        f.close()
        for case in data:
            if not case["isSkip"]:
                test_cases.append(case)
        ids = [test["testName"] for test in test_cases]
        metafunc.parametrize("test_case", test_cases, ids=ids)


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # Execute all other hooks to obtain the report object
    # pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])
    # Check if the test failed
    if report.when == "call" or report.when == "setup":
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
            m = re.search(r"\[([A-Za-z0-9_]+)\]", item.nodeid)
            test_case = m.group(1)
            file_name = Path.cwd().joinpath("screenshots").joinpath(test_case + ".png")
            driver.get_screenshot_as_file(file_name)
            if file_name:
                html = "<div><img src='%s' alt='screenshot' style='width:304px;height:228px;'" \
                        "onclick='window.open(this.src)' align='right'/></div>" % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def pytest_html_report_title(report):
    report.title = "Orange HRM Test Automation"



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


