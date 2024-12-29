import allure

from utilities.event_listener import EventListener
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver
import pytest
import selenium.webdriver
from utilities.common_ops import get_data, get_time_stamp
from selenium.webdriver import ActionChains
from utilities.manage_page import ManagerPages
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

web_driver = None
action = None


@pytest.fixture(scope='class')
def init_web_driver(request):
    edriver = get_web_driver()
    globals()['web_driver'] = EventFiringWebDriver(edriver, EventListener())
    web_driver = globals()['web_driver']
    web_driver.maximize_window()
    web_driver.get(get_data('URL'))
    request.cls.web_driver = web_driver
    globals()['action'] = ActionChains(web_driver)
    ManagerPages.init_web_pages()
    web_driver.implicitly_wait(3)
    yield
    web_driver.quit()


def get_web_driver():
    web_browser = get_data('Browser').lower()
    if web_browser.lower() == "chrome":
        web_driver = get_chrome()
    elif web_browser.lower() == 'firefox':
        web_driver = get_firefox()
    elif web_browser.lower() == 'edge':
        web_driver = get_edge()
    else:
        web_driver = None
        raise Exception('Wrong Input, Unrecognized Browser')
    return web_driver


def get_chrome():
    srv = Service(ChromeDriverManager().install())
    chrome_driver = selenium.webdriver.Chrome(service=srv)
    # chrome_driver = selenium.webdriver.Chrome(ChromeDriverManager().install())
    return chrome_driver


def get_firefox():
    srv = Service(executable_path=GeckoDriverManager().install())
    ff_driver = selenium.webdriver.Firefox(service=srv)
    return ff_driver


def get_edge():
    srv = Service(EdgeChromiumDriverManager().install())
    edge_driver = selenium.webdriver.Firefox(service=srv)
    return edge_driver


# catch exceptions and errors
# def pytest_exception_interact(node, call, report):
#     if report.failed:
#         if globals()['web_driver'] is not None:  # if it is NONE --> API rest
#             image = get_data('ScreenShort_Path') + 'screen_' + str(get_time_stamp()) + '.png'
#             globals()['web_driver'].get_screenshot_as_file(image)
#             allure.attach.file(image, attachment_type=allure.attachment_type.PNG)