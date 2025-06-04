import time
from datetime import datetime

import pytest

from pages.AccountSuccessPage import AccountSuccessPage
from pages.HomePage import HomePage
from pages.RegisterPage import RegisterPage


@pytest.mark.usefixtures("setup_and_teardown")
class TestRegister:
    def test_create_account_with_mandatory_fields(self):
        home_page = HomePage(self.driver)
        home_page.click_on_link_my_account()
        home_page.click_on_link_register()

        register_page = RegisterPage(self.driver)
        register_page.enter_first_name("Alex")
        register_page.enter_last_name("Smith")
        register_page.enter_email(self.generate_email_with_time_stamp())
        register_page.enter_telephone("0123456789")
        register_page.enter_password("12345")
        register_page.enter_confirm_password("12345")
        register_page.click_radio_button_agree()
        # register_page.click_checkbox_privacy_policy()
        register_page.click_button_continue()

        time.sleep(2)

        account_success_page = AccountSuccessPage(self.driver)
        expected_message = "Your Account Has Been Created!"
        assert expected_message in account_success_page.display_header_message()

    def test_create_account_by_providing_all_fields(self):
        home_page = HomePage(self.driver)
        home_page.click_on_link_my_account()
        home_page.click_on_link_register()

        register_page = RegisterPage(self.driver)
        register_page.enter_first_name("Alex")
        register_page.enter_last_name("Smith")
        register_page.enter_email(self.generate_email_with_time_stamp())
        register_page.enter_telephone("0123456789")
        register_page.enter_password("12345")
        register_page.enter_confirm_password("12345")
        register_page.click_yes_radio_button()
        register_page.click_checkbox_privacy_policy()
        register_page.click_button_continue()

        time.sleep(2)

        account_success_page = AccountSuccessPage(self.driver)
        expected_message = "Your Account Has Been Created!"
        assert expected_message in account_success_page.display_header_message()

    def test_register_with_duplicate_email(self):
        home_page = HomePage(self.driver)
        home_page.click_on_link_my_account()
        home_page.click_on_link_register()

        register_page = RegisterPage(self.driver)
        register_page.enter_first_name("Alex")
        register_page.enter_last_name("Smith")
        register_page.enter_email("alex.smith@yopmail.com")
        register_page.enter_telephone("0123456789")
        register_page.enter_password("12345")
        register_page.enter_confirm_password("12345")
        register_page.click_yes_radio_button()
        register_page.click_checkbox_privacy_policy()
        register_page.click_button_continue()

        expected_message = "Warning: E-Mail Address is already registered!"
        assert expected_message in register_page.display_warning_duplicate_email()

    def test_without_entering_any_fields(self):
        home_page = HomePage(self.driver)
        home_page.click_on_link_my_account()
        home_page.click_on_link_register()

        register_page = RegisterPage(self.driver)
        register_page.enter_first_name("")
        register_page.enter_last_name("")
        register_page.enter_email("")
        register_page.enter_telephone("")
        register_page.enter_password("")
        register_page.enter_confirm_password("")
        register_page.click_button_continue()

        expected_warning_first_name = "First Name must be between 1 and 32 characters!"
        assert register_page.display_warning_first_name() in expected_warning_first_name

        expected_warning_last_name = "Last Name must be between 1 and 32 characters!"
        assert register_page.display_warning_last_name() in expected_warning_last_name

        expected_warning_email = "E-Mail Address does not appear to be valid!"
        assert register_page.display_warning_email() in expected_warning_email

        expected_warning_telephone = "Telephone must be between 3 and 32 characters!"
        assert register_page.display_warning_telephone() in expected_warning_telephone

        expected_warning_password = "Password must be between 4 and 20 characters!"
        assert register_page.display_warning_password() in expected_warning_password

        expected_warning_policy = "Warning: You must agree to the Privacy Policy!"
        assert register_page.display_warning_policy() in expected_warning_policy

    def generate_email_with_time_stamp(self):
        time_stamp = datetime.now().strftime("%Y%m%d%H%M%S")
        return "alex" + time_stamp + "@gmail.com"
