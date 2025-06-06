import time

from pages.HomePage import HomePage
from tests.BaseTest import BaseTest
from utilities import ExcelUtils


class TestRegister(BaseTest):
    def test_create_account_with_mandatory_fields(self):
        home_page = HomePage(self.driver)
        register_page = home_page.navigate_to_register_page()
        account_success_page = register_page.register_an_account(ExcelUtils.get_cell_data("tutorials_ninja_test_data.xlsx", "Sheet2", 2, 1),
                                                                 ExcelUtils.get_cell_data("tutorials_ninja_test_data.xlsx", "Sheet2", 2, 2),
                                                                 self.generate_email_with_time_stamp(),
                                                                 ExcelUtils.get_cell_data("tutorials_ninja_test_data.xlsx", "Sheet2", 2, 3),
                                                                 "12345", "12345", "no", "select")
        time.sleep(2)
        expected_message = "Your Account Has Been Created!"
        assert expected_message in account_success_page.display_header_message()

    def test_create_account_by_providing_all_fields(self):
        home_page = HomePage(self.driver)
        register_page = home_page.navigate_to_register_page()
        account_success_page = register_page.register_an_account("Alex", "Smith", self.generate_email_with_time_stamp(),
                                                                 "0123456789", "12345", "12345", "yes", "select")
        time.sleep(2)
        expected_message = "Your Account Has Been Created!"
        assert expected_message in account_success_page.display_header_message()

    def test_register_with_duplicate_email(self):
        home_page = HomePage(self.driver)
        register_page = home_page.navigate_to_register_page()
        register_page.register_an_account("Alex", "Smith", "alex.smith@yopmail.com",
                                          "0123456789", "12345", "12345", "yes", "select")
        expected_message = "Warning: E-Mail Address is already registered!"
        assert expected_message in register_page.display_warning_duplicate_email()

    def test_without_entering_any_fields(self):
        home_page = HomePage(self.driver)
        register_page = home_page.navigate_to_register_page()
        register_page.register_an_account("", "", "", "", "", "", "no", "no")
        assert register_page.assert_all_warnings("First Name must be between 1 and 32 characters!",
                                                 "Last Name must be between 1 and 32 characters!",
                                                 "E-Mail Address does not appear to be valid!",
                                                 "Telephone must be between 3 and 32 characters!",
                                                 "Password must be between 4 and 20 characters!",
                                                 "Warning: You must agree to the Privacy Policy!")
