from selenium.webdriver.common.by import By

from pages.BasePage import BasePage
from pages.MyAccountPage import MyAccountPage


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    email_field_xpath = "//input[@id='input-email']"
    password_field_xpath = "//input[@id='input-password']"
    login_button_xpath = "//input[@value='Login']"
    warning_message_xpath = "//div[@class='alert alert-danger alert-dismissible']"

    def enter_email_address(self, email):
        self.type_into_element("email_field_xpath", self.email_field_xpath, email)
        # self.driver.find_element(By.XPATH, self.email_field).click()
        # self.driver.find_element(By.XPATH, self.email_field).clear()
        # self.driver.find_element(By.XPATH, self.email_field).send_keys(email)

    def enter_password(self, password):
        self.type_into_element("password_field_xpath", self.password_field_xpath, password)
        # self.driver.find_element(By.XPATH, self.password_field).click()
        # self.driver.find_element(By.XPATH, self.password_field).clear()
        # self.driver.find_element(By.XPATH, self.password_field).send_keys(password)

    def click_login_button(self):
        self.element_click("login_button_xpath", self.login_button_xpath)
        # self.driver.find_element(By.XPATH, self.login_button).click()
        return MyAccountPage(self.driver)

    def display_warning_message(self):
        return self.get_element_text("warning_message_xpath", self.warning_message_xpath)
        # return self.driver.find_element(By.XPATH, self.warning_message).text

    def login_to_application(self, email, password):
        self.enter_email_address(email)
        self.enter_password(password)
        return self.click_login_button()
