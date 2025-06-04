from selenium.webdriver.common.by import By


class RegisterPage:

    def __init__(self, driver):
        self.driver = driver

    text_firstname = "//input[@id='input-firstname']"
    text_lastname = "//input[@id='input-lastname']"
    text_email = "//input[@id='input-email']"
    text_telephone = "//input[@id='input-telephone']"
    text_password = "//input[@id='input-password']"
    text_confirm_password = "//input[@id='input-confirm']"
    radio_button_agree = "//input[@name='agree']"
    button_continue = "//input[@value='Continue']"
    checkbox_privacy_policy = "//input[@name='agree']"
    yes_radio_button = "//label[normalize-space()='Yes']//input[@name='newsletter']"
    warning_duplicate_email = "//div[@class='alert alert-danger alert-dismissible']"
    warning_first_name = "//input[@id='input-firstname']//following-sibling::div"
    warning_last_name = "//input[@id='input-lastname']//following-sibling::div"
    warning_email = "//input[@id='input-email']//following-sibling::div"
    warning_telephone = "//input[@id='input-telephone']//following-sibling::div"
    warning_password = "//input[@id='input-password']//following-sibling::div"
    warning_policy = "//div[@class='alert alert-danger alert-dismissible']"

    def enter_first_name(self, first_name):
        self.driver.find_element(By.XPATH, self.text_firstname).click()
        self.driver.find_element(By.XPATH, self.text_firstname).clear()
        self.driver.find_element(By.XPATH, self.text_firstname).send_keys(first_name)

    def enter_last_name(self, last_name):
        self.driver.find_element(By.XPATH, self.text_lastname).click()
        self.driver.find_element(By.XPATH, self.text_lastname).clear()
        self.driver.find_element(By.XPATH, self.text_lastname).send_keys(last_name)

    def enter_email(self, email):
        self.driver.find_element(By.XPATH, self.text_email).click()
        self.driver.find_element(By.XPATH, self.text_email).clear()
        self.driver.find_element(By.XPATH, self.text_email).send_keys(email)

    def enter_telephone(self, phone):
        self.driver.find_element(By.XPATH, self.text_telephone).click()
        self.driver.find_element(By.XPATH, self.text_telephone).clear()
        self.driver.find_element(By.XPATH, self.text_telephone).send_keys(phone)

    def enter_password(self, password):
        self.driver.find_element(By.XPATH, self.text_password).click()
        self.driver.find_element(By.XPATH, self.text_password).clear()
        self.driver.find_element(By.XPATH, self.text_password).send_keys(password)

    def enter_confirm_password(self, password):
        self.driver.find_element(By.XPATH, self.text_confirm_password).click()
        self.driver.find_element(By.XPATH, self.text_confirm_password).clear()
        self.driver.find_element(By.XPATH, self.text_confirm_password).send_keys(password)

    def click_radio_button_agree(self):
        self.driver.find_element(By.XPATH, self.radio_button_agree).click()

    def click_yes_radio_button(self):
        self.driver.find_element(By.XPATH, self.yes_radio_button).click()

    def click_button_continue(self):
        self.driver.find_element(By.XPATH, self.button_continue).click()

    def click_checkbox_privacy_policy(self):
        self.driver.find_element(By.XPATH, self.checkbox_privacy_policy).click()

    def display_warning_duplicate_email(self):
        return self.driver.find_element(By.XPATH, self.warning_duplicate_email).text

    def display_warning_first_name(self):
        return self.driver.find_element(By.XPATH, self.warning_first_name).text

    def display_warning_last_name(self):
        return self.driver.find_element(By.XPATH, self.warning_last_name).text

    def display_warning_email(self):
        return self.driver.find_element(By.XPATH, self.warning_email).text

    def display_warning_telephone(self):
        return self.driver.find_element(By.XPATH, self.warning_telephone).text

    def display_warning_password(self):
        return self.driver.find_element(By.XPATH, self.warning_password).text

    def display_warning_policy(self):
        return self.driver.find_element(By.XPATH, self.warning_policy).text
