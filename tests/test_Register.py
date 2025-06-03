import time
from datetime import datetime

import pytest
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures("setup_and_teardown")
class TestRegister:
    def test_create_account_with_mandatory_fields(self):
        self.driver.find_element(By.XPATH, "//span[normalize-space()='My Account']").click()
        self.driver.find_element(By.XPATH, "//a[normalize-space()='Register']").click()
        self.driver.find_element(By.XPATH, "//input[@id='input-firstname']").send_keys("Alex")
        self.driver.find_element(By.XPATH, "//input[@id='input-lastname']").send_keys("Smith")
        self.driver.find_element(By.XPATH, "//input[@id='input-email']").send_keys(self.generate_email_with_time_stamp())
        self.driver.find_element(By.XPATH, "//input[@id='input-telephone']").send_keys("0123456789")
        self.driver.find_element(By.XPATH, "//input[@id='input-password']").send_keys("12345")
        self.driver.find_element(By.XPATH, "//input[@id='input-confirm']").send_keys("12345")
        self.driver.find_element(By.XPATH, "//input[@name='agree']").click()
        self.driver.find_element(By.XPATH, "//input[@value='Continue']").click()
        expected_message = "Your Account Has Been Created!"

        time.sleep(2)

        actual_message = self.driver.find_element(By.XPATH, "//div[@id='content']//h1").text
        assert expected_message in actual_message


    def test_create_account_by_providing_all_fields(self):
        self.driver.find_element(By.XPATH, "//span[normalize-space()='My Account']").click()
        self.driver.find_element(By.XPATH, "//a[normalize-space()='Register']").click()
        self.driver.find_element(By.XPATH, "//input[@id='input-firstname']").send_keys("Alex")
        self.driver.find_element(By.XPATH, "//input[@id='input-lastname']").send_keys("Smith")
        self.driver.find_element(By.XPATH, "//input[@id='input-email']").send_keys(self.generate_email_with_time_stamp())
        self.driver.find_element(By.XPATH, "//input[@id='input-telephone']").send_keys("0123456789")
        self.driver.find_element(By.XPATH, "//input[@id='input-password']").send_keys("12345")
        self.driver.find_element(By.XPATH, "//input[@id='input-confirm']").send_keys("12345")
        self.driver.find_element(By.XPATH, "//label[normalize-space()='Yes']//input[@name='newsletter']").click()
        self.driver.find_element(By.XPATH, "//input[@name='agree']").click()
        self.driver.find_element(By.XPATH, "//input[@value='Continue']").click()

        expected_message = "Your Account Has Been Created!"
        actual_message = self.driver.find_element(By.XPATH, "//div[@id='content']//h1").text
        assert expected_message in actual_message


    def test_register_with_duplicate_email(self):
        self.driver.find_element(By.XPATH, "//span[normalize-space()='My Account']").click()
        self.driver.find_element(By.XPATH, "//a[normalize-space()='Register']").click()
        self.driver.find_element(By.XPATH, "//input[@id='input-firstname']").send_keys("Alex")
        self.driver.find_element(By.XPATH, "//input[@id='input-lastname']").send_keys("Smith")
        self.driver.find_element(By.XPATH, "//input[@id='input-email']").send_keys("alex.smith@yopmail.com")
        self.driver.find_element(By.XPATH, "//input[@id='input-telephone']").send_keys("0123456789")
        self.driver.find_element(By.XPATH, "//input[@id='input-password']").send_keys("P@ssw0rd#123")
        self.driver.find_element(By.XPATH, "//input[@id='input-confirm']").send_keys("P@ssw0rd#123")
        self.driver.find_element(By.XPATH, "//label[normalize-space()='Yes']//input[@name='newsletter']").click()
        self.driver.find_element(By.XPATH, "//input[@name='agree']").click()
        self.driver.find_element(By.XPATH, "//input[@value='Continue']").click()

        expected_message = "Warning: E-Mail Address is already registered!"
        actual_message = self.driver.find_element(By.XPATH, "//div[@class='alert alert-danger alert-dismissible']").text
        assert expected_message in actual_message


    def test_without_entering_any_fields(self):
        self.driver.find_element(By.XPATH, "//span[normalize-space()='My Account']").click()
        self.driver.find_element(By.XPATH, "//a[normalize-space()='Register']").click()
        self.driver.find_element(By.XPATH, "//input[@id='input-firstname']").send_keys("")
        self.driver.find_element(By.XPATH, "//input[@id='input-lastname']").send_keys("")
        self.driver.find_element(By.XPATH, "//input[@id='input-email']").send_keys("")
        self.driver.find_element(By.XPATH, "//input[@id='input-telephone']").send_keys("")
        self.driver.find_element(By.XPATH, "//input[@id='input-password']").send_keys("")
        self.driver.find_element(By.XPATH, "//input[@id='input-confirm']").send_keys("")
        self.driver.find_element(By.XPATH, "//input[@value='Continue']").click()

        expected_warning_first_name = "First Name must be between 1 and 32 characters!"
        actual_warning_first_name = self.driver.find_element(By.XPATH,
                                                        "//input[@id='input-firstname']//following-sibling::div").text
        assert actual_warning_first_name in expected_warning_first_name

        expected_warning_last_name = "Last Name must be between 1 and 32 characters!"
        actual_warning_last_name = self.driver.find_element(By.XPATH,
                                                       "//input[@id='input-lastname']//following-sibling::div").text
        assert actual_warning_last_name in expected_warning_last_name

        expected_warning_email = "E-Mail Address does not appear to be valid!"
        actual_warning_email = self.driver.find_element(By.XPATH, "//input[@id='input-email']//following-sibling::div").text
        assert actual_warning_email in expected_warning_email

        expected_warning_telephone = "Telephone must be between 3 and 32 characters!"
        actual_warning_telephone = self.driver.find_element(By.XPATH,
                                                       "//input[@id='input-telephone']//following-sibling::div").text
        assert actual_warning_telephone in expected_warning_telephone

        expected_warning_password = "Password must be between 4 and 20 characters!"
        actual_warning_password = self.driver.find_element(By.XPATH,
                                                      "//input[@id='input-password']//following-sibling::div").text
        assert actual_warning_password in expected_warning_password

        expected_warning_policy = "Warning: You must agree to the Privacy Policy!"
        actual_warning_policy = self.driver.find_element(By.XPATH, "//div[@class='alert alert-danger alert-dismissible']").text
        assert actual_warning_policy in expected_warning_policy


    def generate_email_with_time_stamp(self):
        time_stamp = datetime.now().strftime("%Y%m%d%H%M%S")
        return "alex" + time_stamp + "@gmail.com"
