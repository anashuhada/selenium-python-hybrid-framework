from selenium.webdriver.common.by import By


class AccountSuccessPage:

    def __init__(self, driver):
        self.driver = driver

    header_message = "//div[@id='content']//h1"

    def display_header_message(self):
        return self.driver.find_element(By.XPATH, self.header_message).text
