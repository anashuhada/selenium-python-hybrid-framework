import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from utilities import ReadConfigurations


@pytest.fixture()
def setup_and_teardown(request):
    # global driver
    browser = ReadConfigurations.read_configuration("basic info", "browser")

    if browser == "chrome":
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    elif browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "edge":
        driver = webdriver.Edge()
    else:
        raise Exception("Invalid browser, please provide a valid browser in config.")

    driver.maximize_window()
    url = ReadConfigurations.read_configuration("basic info", "url")
    driver.get(url)
    request.cls.driver = driver  # important: make driver available to the test class
    yield
    time.sleep(3)
    driver.quit()
