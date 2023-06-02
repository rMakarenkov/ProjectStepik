from selenium import  webdriver
from selenium.webdriver.common.by import By
from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        get_url = self.browser.current_url
        assert "/accounts/login/" in str(get_url), "Invalid transition. This page " \
                                        "is not an authorization / registration page"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM_LINK)

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM_LINK)

    def register_new_user(self, login, password):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM_LINK)

        e_mail_input = self.browser.find_element(By.CSS_SELECTOR, "#id_registration-email")
        e_mail_input.send_keys(login)

        password_input = self.browser.find_element(By.CSS_SELECTOR, "#id_registration-password1")
        password_input.send_keys(password)

        d_password_input = self.browser.find_element(By.CSS_SELECTOR, "#id_registration-password2")
        d_password_input.send_keys(password)

        button_reg = self.browser.find_element(*LoginPageLocators.BUTTON_REG_NEW_USER)
        button_reg.click()

    def user_logged_in_site(self):
        assert self.is_element_present()



