from pages.BasePage import BasePage


class MyAccountPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    my_account_header_xpath = "//h2[normalize-space()='My Account']"

    def my_account_header_exist(self):
        return self.check_display_status("my_account_header_xpath", self.my_account_header_xpath)
        # return self.driver.find_element(By.XPATH, self.my_account_header).is_displayed()
