import time
from datetime import datetime

import pytest

from pages.HomePage import HomePage


@pytest.mark.usefixtures("setup_and_teardown")
class TestLogin:
    def test_login_with_valid_credentials(self):
        home_page = HomePage(self.driver)
        login_page = home_page.navigate_to_login_page()
        my_account_page = login_page.login_to_application("alex.smith@yopmail.com", "P@ssw0rd#123")
        time.sleep(2)
        assert my_account_page.my_account_header_exist()

    def test_login_with_invalid_email_and_valid_password(self):
        home_page = HomePage(self.driver)
        login_page = home_page.navigate_to_login_page()
        login_page.login_to_application(self.generate_email_with_time_stamp(), "P@ssw0rd#123")
        time.sleep(2)
        expected_message = "Warning: No match for E-Mail Address and/or Password."
        assert login_page.display_warning_message().__contains__(expected_message)

    def test_login_with_valid_email_and_invalid_password(self):
        home_page = HomePage(self.driver)
        login_page = home_page.navigate_to_login_page()
        login_page.login_to_application("alex.smith@yopmail.com", "P@ssw0rd123")
        time.sleep(2)
        expected_message = "Warning: No match for E-Mail Address and/or Password."
        assert login_page.display_warning_message().__eq__(expected_message)

    def test_login_without_providing_credentials(self):
        home_page = HomePage(self.driver)
        login_page = home_page.navigate_to_login_page()
        login_page.login_to_application("", "")
        time.sleep(2)
        expected_message = "Warning: No match for E-Mail Address and/or Password."
        assert login_page.display_warning_message().__eq__(expected_message)

    def generate_email_with_time_stamp(self):
        time_stamp = datetime.now().strftime("%Y%m%d%H%M%S")
        return "alex" + time_stamp + "@gmail.com"
