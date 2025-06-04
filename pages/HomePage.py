from selenium.webdriver.common.by import By

from pages.SearchPage import SearchPage


class HomePage:
    def __init__(self, driver): # constructor
        self.driver = driver

    search_box_field_name = "//input[@placeholder='Search']"
    search_button = "//button[@class='btn btn-default btn-lg']"
    link_my_account = "//span[normalize-space()='My Account']"
    link_login = "//a[normalize-space()='Login']"
    link_register = "//a[normalize-space()='Register']"

    def enter_product_into_search_box_field(self, product_name):
        self.driver.find_element(By.XPATH, self.search_box_field_name).click()
        self.driver.find_element(By.XPATH, self.search_box_field_name).clear()
        self.driver.find_element(By.XPATH, self.search_box_field_name).send_keys(product_name)

    def click_on_search_button(self):
        self.driver.find_element(By.XPATH, self.search_button).click()
        return SearchPage(self.driver)

    def click_on_link_my_account(self):
        self.driver.find_element(By.XPATH, self.link_my_account).click()

    def click_on_link_login(self):
        self.driver.find_element(By.XPATH, self.link_login).click()
        return HomePage(self.driver)

    def click_on_link_register(self):
        self.driver.find_element(By.XPATH, self.link_register).click()