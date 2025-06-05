from selenium.webdriver.common.by import By

from pages.BasePage import BasePage


class SearchPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    product_link_text_xpath = "//div[@class='caption']//h4//a"
    product_message_xpath = "//input[@type='button']/following-sibling::p"

    def display_status_of_product(self):
        return self.check_display_status("product_link_text_xpath", self.product_link_text_xpath)
        # return self.driver.find_element(By.XPATH, self.product_link_text).is_displayed()

    def display_no_product_message(self):
        return self.get_element_text("product_message_xpath", self.product_message_xpath)
        # return self.driver.find_element(By.XPATH, self.product_message).text
