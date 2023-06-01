from pages.base_page import BasePage
from pages.locators import MainPageLocators
from .login_page import LoginPage
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException


class MainPage(BasePage):
    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()
        try:
            alert = self.browser.switch_to.alert()
            alert.accept()
            print("Accepted alert")
        except NoAlertPresentException:
            print("No alert")

    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"
