import time

from selenium.webdriver.common.by import By

from pages.AccountSuccessPage import AccountSuccessPage
from pages.BasePage import BasePage


class RegisterPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    text_firstname_xpath = "//input[@id='input-firstname']"
    text_lastname_xpath = "//input[@id='input-lastname']"
    text_email_xpath = "//input[@id='input-email']"
    text_telephone_xpath = "//input[@id='input-telephone']"
    text_password_xpath = "//input[@id='input-password']"
    text_confirm_password_xpath = "//input[@id='input-confirm']"
    radio_button_agree_xpath = "//input[@name='agree']"
    button_continue_xpath = "//input[@value='Continue']"
    checkbox_privacy_policy_xpath = "//input[@name='agree']"
    yes_radio_button_xpath = "//label[normalize-space()='Yes']//input[@name='newsletter']"
    warning_duplicate_email_xpath = "//div[@class='alert alert-danger alert-dismissible']"
    warning_first_name_xpath = "//input[@id='input-firstname']/following-sibling::div"
    warning_last_name_xpath = "//input[@id='input-lastname']/following-sibling::div"
    warning_email_xpath = "//input[@id='input-email']/following-sibling::div"
    warning_telephone_xpath = "//input[@id='input-telephone']/following-sibling::div"
    warning_password_xpath = "//input[@id='input-password']/following-sibling::div"
    warning_policy_xpath = "//div[@class='alert alert-danger alert-dismissible']"

    def enter_first_name(self, first_name):
        self.type_into_element("text_firstname_xpath", self.text_firstname_xpath, first_name)
        # self.driver.find_element(By.XPATH, self.text_firstname).click()
        # self.driver.find_element(By.XPATH, self.text_firstname).clear()
        # self.driver.find_element(By.XPATH, self.text_firstname).send_keys(first_name)

    def enter_last_name(self, last_name):
        self.type_into_element("text_lastname_xpath", self.text_lastname_xpath, last_name)
        # self.driver.find_element(By.XPATH, self.text_lastname).click()
        # self.driver.find_element(By.XPATH, self.text_lastname).clear()
        # self.driver.find_element(By.XPATH, self.text_lastname).send_keys(last_name)

    def enter_email(self, email):
        self.type_into_element("text_email_xpath", self.text_email_xpath, email)
        # self.driver.find_element(By.XPATH, self.text_email).click()
        # self.driver.find_element(By.XPATH, self.text_email).clear()
        # self.driver.find_element(By.XPATH, self.text_email).send_keys(email)

    def enter_telephone(self, phone):
        self.type_into_element("text_telephone_xpath", self.text_telephone_xpath, phone)
        # self.driver.find_element(By.XPATH, self.text_telephone).click()
        # self.driver.find_element(By.XPATH, self.text_telephone).clear()
        # self.driver.find_element(By.XPATH, self.text_telephone).send_keys(phone)

    def enter_password(self, password):
        self.type_into_element("text_password_xpath", self.text_password_xpath, password)
        # self.driver.find_element(By.XPATH, self.text_password).click()
        # self.driver.find_element(By.XPATH, self.text_password).clear()
        # self.driver.find_element(By.XPATH, self.text_password).send_keys(password)

    def enter_confirm_password(self, password):
        self.type_into_element("text_confirm_password_xpath", self.text_confirm_password_xpath, password)
        # self.driver.find_element(By.XPATH, self.text_confirm_password).click()
        # self.driver.find_element(By.XPATH, self.text_confirm_password).clear()
        # self.driver.find_element(By.XPATH, self.text_confirm_password).send_keys(password)

    def click_radio_button_agree(self):
        self.element_click("radio_button_agree_xpath", self.radio_button_agree_xpath)
        # self.driver.find_element(By.XPATH, self.radio_button_agree).click()

    def click_yes_radio_button(self):
        self.element_click("yes_radio_button_xpath", self.yes_radio_button_xpath)
        # self.driver.find_element(By.XPATH, self.yes_radio_button).click()

    def click_button_continue(self):
        self.element_click("button_continue_xpath", self.button_continue_xpath)
        # self.driver.find_element(By.XPATH, self.button_continue).click()
        return AccountSuccessPage(self.driver)

    def click_checkbox_privacy_policy(self):
        self.element_click("checkbox_privacy_policy_xpath", self.checkbox_privacy_policy_xpath)
        # self.driver.find_element(By.XPATH, self.checkbox_privacy_policy).click()

    def display_warning_duplicate_email(self):
        return self.get_element_text("warning_duplicate_email_xpath", self.warning_duplicate_email_xpath)
        # return self.driver.find_element(By.XPATH, self.warning_duplicate_email).text

    def display_warning_first_name(self):
        return self.get_element_text("warning_first_name_xpath", self.warning_first_name_xpath)
        # return self.driver.find_element(By.XPATH, self.warning_first_name).text

    def display_warning_last_name(self):
        return self.get_element_text("warning_last_name_xpath", self.warning_last_name_xpath)
        # return self.driver.find_element(By.XPATH, self.warning_last_name).text

    def display_warning_email(self):
        return self.get_element_text("warning_email_xpath", self.warning_email_xpath)
        # return self.driver.find_element(By.XPATH, self.warning_email).text

    def display_warning_telephone(self):
        return self.get_element_text("warning_telephone_xpath", self.warning_telephone_xpath)
        # return self.driver.find_element(By.XPATH, self.warning_telephone).text

    def display_warning_password(self):
        return self.get_element_text("warning_password_xpath", self.warning_password_xpath)
        # return self.driver.find_element(By.XPATH, self.warning_password).text

    def display_warning_policy(self):
        return self.get_element_text("warning_policy_xpath", self.warning_policy_xpath)
        # return self.driver.find_element(By.XPATH, self.warning_policy).text

    def register_an_account(self, firstname, lastname, email, phone, password, confirm_password, yes_or_no,
                            privacy_policy):
        self.enter_first_name(firstname)
        self.enter_last_name(lastname)
        self.enter_email(email)
        self.enter_telephone(phone)
        self.enter_password(password)
        self.enter_confirm_password(confirm_password)

        if yes_or_no.__eq__("yes"):
            self.click_yes_radio_button()

        if privacy_policy.__eq__("select"):
            self.click_checkbox_privacy_policy()

        return self.click_button_continue()

    def assert_all_warnings(self, ew_first_name, ew_last_name, ew_email, ew_telephone, ew_password, ew_policy):
        aw_first_name = self.display_warning_first_name()
        aw_last_name = self.display_warning_last_name()
        aw_email = self.display_warning_email()
        aw_telephone = self.display_warning_telephone()
        aw_password = self.display_warning_password()
        aw_policy = self.display_warning_policy()

        status = False

        time.sleep(2)
        if ew_policy.__contains__(aw_policy):
            time.sleep(2)
            if ew_first_name.__eq__(aw_first_name):
                time.sleep(2)
                if ew_last_name.__eq__(aw_last_name):
                    time.sleep(2)
                    if ew_email.__eq__(aw_email):
                        time.sleep(2)
                        if ew_telephone.__eq__(aw_telephone):
                            time.sleep(2)
                            if ew_password.__eq__(aw_password):
                                status = True

        return status
