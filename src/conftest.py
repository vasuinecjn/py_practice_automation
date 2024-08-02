import os
import settings
import json
from pathlib import Path
import re
import logging
from datetime import datetime
import pytest
import pytest_html
from selenium import webdriver
from src.application import Application
from src.web_operations import WebOperation
from zipfile import ZipFile, ZIP_DEFLATED

driver = None


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default=settings.browser)
    parser.addoption("--click_screenshot", action="store", default=settings.click_screenshot)


def load_page_data():
    page_data_dict = {}
    data_path = Path.cwd().joinpath("test_data").joinpath("testData.json")
    with open(data_path, "r") as f:
        data = json.load(f)
    f.close()
    for k in data.keys():
        for ki, v in data[k].items():
            page_data_dict[ki] = v
    return page_data_dict


@pytest.fixture(scope='function')
def screenshot_dir(request):
    test_name = request.node.name
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    screenshot_dir = os.path.join(Path.cwd().joinpath("screenshots"), test_name, timestamp)
    os.makedirs(screenshot_dir, exist_ok=True)
    return screenshot_dir


@pytest.fixture(scope='function')
def logger(request):
    test_name = request.node.name
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_file = Path.cwd().joinpath("logs").joinpath(f"{test_name}_{timestamp}.log")
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    # Create file handler which logs even debug messages
    fh = logging.FileHandler(log_file)
    fh.setLevel(logging.DEBUG)
    # Create console handler with a higher log level
    ch = logging.StreamHandler()
    ch.setLevel(logging.ERROR)
    # Create formatter and add it to the handlers
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)
    # Add the handlers to logger
    logger.addHandler(fh)
    logger.addHandler(ch)
    yield logger
    # Remove handlers after test to avoid duplicate logs in subsequent tests
    logger.removeHandler(fh)
    logger.removeHandler(ch)


@pytest.fixture(scope="function")
def init_test(request, logger, screenshot_dir):
    global driver
    browser = request.config.getoption("--browser")
    flag_dict = {"click_screenshot": request.config.getoption("--click_screenshot"),
                 "browser": browser}
    match browser:
        case "chrome":
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument("ignore-certificate-errors")
            driver = webdriver.Chrome(options=chrome_options)
        case "firefox":
            firefox_options = webdriver.FirefoxOptions()
            firefox_options.add_argument("ignore-certificate-errors")
            driver = webdriver.Firefox(options=firefox_options)
        case _:
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument("ignore-certificate-errors")
            driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    logger = logger
    web_op = WebOperation(driver, flag_dict, logger, screenshot_dir)
    request.cls.application = Application(web_op, load_page_data())
    yield
    driver.close()
    driver.quit()
    zip_filename = f"{os.path.basename(screenshot_dir)}_{request.node.name}.zip"
    zip_filepath = os.path.join(str(Path(screenshot_dir).parent), zip_filename)
    with ZipFile(zip_filepath, mode="w", compression=ZIP_DEFLATED) as ss_zip_file:
        for file in Path(screenshot_dir).glob("*.png"):
            ss_zip_file.write(file, arcname=file.name)
        ss_zip_file.close()


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
    print(item.funcargs)
    print(item.cls.application.web_op.screenshot_dir if hasattr(item.cls.application.web_op, "screenshot_dir") else "no screen shot directory")
    # zip_filepath = None
    if hasattr(item.cls.application.web_op, "screenshot_dir") :
        ss_dir = item.cls.application.web_op.screenshot_dir
        zip_filename = f"{os.path.basename(ss_dir)}_{item.name}.zip"
        zip_filepath = os.path.join(str(Path(ss_dir).parent), zip_filename)
    else:
        zip_filepath = None
    ss_zip = "<div><img src='%s' alt='zip_screenshot' style='width:80px;height:80px;'" \
           "onclick='window.open(this.src)' align='right'/></div>" % zip_filepath
    extra = getattr(report, "extra", [])
    extra.append(pytest_html.extras.html(ss_zip))
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
