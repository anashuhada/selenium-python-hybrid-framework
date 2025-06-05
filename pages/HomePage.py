from selenium.webdriver.common.by import By

from pages.BasePage import BasePage
from pages.LoginPage import LoginPage
from pages.RegisterPage import RegisterPage
from pages.SearchPage import SearchPage


class HomePage(BasePage):
    def __init__(self, driver):  # constructor
        # self.driver = driver
        super().__init__(driver)

    search_box_field_name_xpath = "//input[@placeholder='Search']"
    search_button_xpath = "//button[@class='btn btn-default btn-lg']"
    link_my_account_xpath = "//span[normalize-space()='My Account']"
    link_login_xpath = "//a[normalize-space()='Login']"
    link_register_xpath = "//a[normalize-space()='Register']"

    def enter_product_into_search_box_field(self, product_name):
        # self.driver.find_element(By.XPATH, self.search_box_field_name).click()
        # self.driver.find_element(By.XPATH, self.search_box_field_name).clear()
        # self.driver.find_element(By.XPATH, self.search_box_field_name).send_keys(product_name)
        self.type_into_element("search_box_field_name_xpath", self.search_box_field_name_xpath, product_name)

    def click_on_search_button(self):
        self.element_click("search_button_xpath", self.search_button_xpath)
        # self.driver.find_element(By.XPATH, self.search_button).click()
        return SearchPage(self.driver)

    def click_on_link_my_account(self):
        self.element_click("link_my_account_xpath", self.link_my_account_xpath)
        # self.driver.find_element(By.XPATH, self.link_my_account).click()

    def click_on_link_login(self):
        self.element_click("link_login_xpath", self.link_login_xpath)
        # self.driver.find_element(By.XPATH, self.link_login).click()
        return LoginPage(self.driver)

    def click_on_link_register(self):
        self.element_click("link_register_xpath", self.link_register_xpath)
        # self.driver.find_element(By.XPATH, self.link_register).click()
        return RegisterPage(self.driver)

    def search_for_a_product(self, product_name):
        self.enter_product_into_search_box_field(product_name)
        return self.click_on_search_button()

    def navigate_to_login_page(self):
        self.click_on_link_my_account()
        return self.click_on_link_login()

    def navigate_to_register_page(self):
        self.click_on_link_my_account()
        return self.click_on_link_register()
