import time
import pytest
import allure

from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from utilities import ReadConfigurations


@pytest.fixture()
def setup_and_teardown(request):
    browser = ReadConfigurations.read_configuration("basic info", "browser")
    url = ReadConfigurations.read_configuration("basic info", "url")

    if browser == "chrome":
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    elif browser == "firefox":
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    elif browser == "edge":
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
    else:
        raise Exception("Invalid browser, please provide a valid browser in config.ini")

    driver.maximize_window()
    driver.get(url)
    request.cls.driver = driver  # make driver available to test class

    yield

    # Capture screenshot on failure
    if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
        allure.attach(driver.get_screenshot_as_png(),
                      name="failure_screenshot",
                      attachment_type=AttachmentType.PNG)

    time.sleep(2)
    driver.quit()


# Needed to hook test result state into request.node
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)


# If you still want CLI browser override:
def pytest_addoption(parser):
    parser.addoption("--browser", help="Browser to run tests on (overrides config.ini)")
