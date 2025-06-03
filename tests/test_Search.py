import pytest
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures("setup_and_teardown")
class TestSearch:
    def test_search_for_a_valid_product(self):
        self.driver.find_element(By.XPATH, "//input[@placeholder='Search']").send_keys("HP")
        self.driver.find_element(By.XPATH, "//button[@class='btn btn-default btn-lg']").click()
        assert self.driver.find_element(By.XPATH, "//a[normalize-space()='HP LP3065']").is_displayed()


    def test_search_for_an_invalid_product(self):
        self.driver.find_element(By.XPATH, "//input[@placeholder='Search']").send_keys("Honda")
        self.driver.find_element(By.XPATH, "//button[@class='btn btn-default btn-lg']").click()

        expected_text = "There is no product that matches the search criteria."
        actual_text = self.driver.find_element(By.XPATH, "//input[@type='button']/following-sibling::p").text
        assert actual_text.__eq__(expected_text)


    def test_search_without_providing_any_product(self):
        self.driver.find_element(By.XPATH, "//input[@placeholder='Search']").send_keys("")
        self.driver.find_element(By.XPATH, "//button[@class='btn btn-default btn-lg']").click()

        expected_text = "There is no product that matches the search criteria."
        actual_text = self.driver.find_element(By.XPATH, "//input[@type='button']/following-sibling::p").text
        assert actual_text.__eq__(expected_text)
