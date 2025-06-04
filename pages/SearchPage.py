from selenium.webdriver.common.by import By


class SearchPage:
    def __init__(self, driver):
        self.driver = driver

    product_link_text = "HP LP3065"
    product_message = "//input[@type='button']/following-sibling::p"

    def display_status_of_product(self):
        return self.driver.find_element(By.XPATH, self.product_link_text).is_displayed()

    def display_no_product_message(self):
        return self.driver.find_element(By.XPATH, self.product_message).text
