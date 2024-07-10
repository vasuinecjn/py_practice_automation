import pytest
from selenium import webdriver
from pytest_metadata.plugin import metadata_key
from browsermobproxy import Server
import socket


def get_free_tcp_port():
    s = socket.socket()
    s.bind(('', 0))
    addr = s.getsockname()
    s.close()
    print('\nrunning server in this port {0}'.format(addr[1]))
    return addr[1]


@pytest.fixture()
def setup(browser):
    # server = Server('//browsermob-proxy-2.1.4/bin/browsermob-proxy',
    #                 {'port': get_free_tcp_port()})
    # server.start()
    # proxy = server.create_proxy(params={'trustAllServers': 'true'})
    match browser:
        case 'chrome':
            chrome_options = webdriver.ChromeOptions()
            # chrome_options.add_argument('--proxy-server={0}'.format(proxy.proxy))
            chrome_options.add_argument('ignore-certificate-errors')
            driver = webdriver.Chrome(options=chrome_options)
        case 'firefox':
            driver = webdriver.Firefox()
        case _:
            chrome_options = webdriver.ChromeOptions()
            # chrome_options.add_argument('--proxy-server={0}'.format(proxy.proxy))
            chrome_options.add_argument('ignore-certificate-errors')
            driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.close()
    driver.quit()
    # proxy.close()
    # server.stop()


def pytest_addoption(parser):  #This will get the value from CLI /hooks
    parser.addoption('--browser')


@pytest.fixture()
def browser(request):  # This will return the Browser value to setup method
    return request.config.getoption('--browser')


### pyTest html report ###

# It is hook for adding environment info to HTML Report
def pytest_configure(config):
    config.stash[metadata_key]['Project Name'] = 'nop Commerce'
    config.stash[metadata_key]['Module Name'] = 'Customers'
    config.stash[metadata_key]['Tester'] = 'Sjn'


# It is hook for delete/Modify Environment info to HTML Report
@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop('JAVA_HOME', None)
    metadata.pop('Plugins', None)


if __name__ == '__main__':
    get_free_tcp_port()
