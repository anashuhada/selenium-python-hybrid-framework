import time
from datetime import datetime

import pytest

from pages.HomePage import HomePage
from pages.LoginPage import LoginPage
from pages.MyAccountPage import MyAccountPage


@pytest.mark.usefixtures("setup_and_teardown")
class TestLogin:
    def test_login_with_valid_credentials(self):
        home_page = HomePage(self.driver)
        home_page.click_on_link_my_account()
        login_page = home_page.click_on_link_login()

        # login_page = LoginPage(self.driver)
        login_page.enter_email_address("alex.smith@yopmail.com")
        login_page.enter_password("P@ssw0rd#123")
        login_page.click_login_button()

        time.sleep(2)

        my_account_page = MyAccountPage(self.driver)
        assert my_account_page.my_account_header_exist()

    def test_login_with_invalid_email_and_valid_password(self):
        home_page = HomePage(self.driver)
        home_page.click_on_link_my_account()
        home_page.click_on_link_login()

        login_page = LoginPage(self.driver)
        login_page.enter_email_address(self.generate_email_with_time_stamp())
        login_page.enter_password("P@ssw0rd#123")
        login_page.click_login_button()

        time.sleep(2)

        expected_message = "Warning: No match for E-Mail Address and/or Password."
        assert login_page.display_warning_message().__contains__(expected_message)

    def test_login_with_valid_email_and_invalid_password(self):
        home_page = HomePage(self.driver)
        home_page.click_on_link_my_account()
        home_page.click_on_link_login()

        login_page = LoginPage(self.driver)
        login_page.enter_email_address("alex.smith@yopmail.com")
        login_page.enter_password("P@ssw0rd123")
        login_page.click_login_button()

        time.sleep(2)

        expected_message = "Warning: No match for E-Mail Address and/or Password."
        assert login_page.display_warning_message().__eq__(expected_message)

    def test_login_without_providing_credentials(self):
        home_page = HomePage(self.driver)
        home_page.click_on_link_my_account()
        home_page.click_on_link_login()

        login_page = LoginPage(self.driver)
        login_page.enter_email_address("")
        login_page.enter_password("")
        login_page.click_login_button()

        time.sleep(2)

        expected_message = "Warning: No match for E-Mail Address and/or Password."
        assert login_page.display_warning_message().__eq__(expected_message)

    def generate_email_with_time_stamp(self):
        time_stamp = datetime.now().strftime("%Y%m%d%H%M%S")
        return "alex" + time_stamp + "@gmail.com"
