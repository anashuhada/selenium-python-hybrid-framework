from selenium.webdriver.common.by import By


class MyAccountPage:

    def __init__(self, driver):
        self.driver = driver

    my_account_header = "//h2[normalize-space()='My Account']"

    def my_account_header_exist(self):
        return self.driver.find_element(By.XPATH, self.my_account_header).is_displayed()
