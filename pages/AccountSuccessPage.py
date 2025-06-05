from selenium.webdriver.common.by import By

from pages.BasePage import BasePage


class AccountSuccessPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    header_message_xpath = "//div[@id='content']//h1"

    def display_header_message(self):
        return self.get_element_text("header_message_xpath", self.header_message_xpath)
        # return self.driver.find_element(By.XPATH, self.header_message).text
