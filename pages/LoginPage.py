from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    email_field = "//input[@id='input-email']"
    password_field = "//input[@id='input-password']"
    login_button = "//input[@value='Login']"
    warning_message = "//div[@class='alert alert-danger alert-dismissible']"

    def enter_email_address(self, email):
        self.driver.find_element(By.XPATH, self.email_field).click()
        self.driver.find_element(By.XPATH, self.email_field).clear()
        self.driver.find_element(By.XPATH, self.email_field).send_keys(email)

    def enter_password(self, password):
        self.driver.find_element(By.XPATH, self.password_field).click()
        self.driver.find_element(By.XPATH, self.password_field).clear()
        self.driver.find_element(By.XPATH, self.password_field).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(By.XPATH, self.login_button).click()

    def display_warning_message(self):
        return self.driver.find_element(By.XPATH, self.warning_message).text
