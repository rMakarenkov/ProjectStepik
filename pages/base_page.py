import time
import random

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from pages.locators import BasePageLocators


class BasePage():

    # конструктор, метод который вызывается, когда мы создаем объект
    def __init__(self, browser, url, timeout=5):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    # метод, который должен вручную открывать страницу
    def open(self):
        self.browser.get(self.url)

    # метод, для неявного ожидания со значением по умолчанию - 10

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def is_element_present_text(self, how, what):
        try:
            element = self.browser.find_element(how, what)
            element_text = element.text
        except NoSuchElementException:
            return None
        return element_text

    # абстрактный метод, который проверяет, что элемент не появляется на странице в течении заданного времени
    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(ec.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    # абстрактный метод, который позволяет проверить, что элемент исчезает на странице в течении заданного времени
    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).until_not(
                ec.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def go_to_login_page(self):
        login_link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        login_link.click()
        try:
            alert = self.browser.switch_to.alert()
            alert.accept()
            print("Accepted alert")
        except NoAlertPresentException:
            print("No alert")

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), "Login link is not presented"

    def go_to_basket_page(self):
        basket_link = self.browser.find_element(*BasePageLocators.BASKET_LINK)
        basket_link.click()
        try:
            alert = self.browser.switch_to.alert()
            alert.accept()
            print("Accepted alert")
        except NoAlertPresentException:
            print("No alert")

    # проверка, что пользователь залогинен
    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented," \
                                                                     " probably unauthorised user"

    def generate_email(self):
        email = str(time.time()) + "@fakemail.org"
        return email

    def generate_password(self):
        pas = ''
        for i in range(16):  # Количество символов (16)
            pas = pas + random.choice(list(
                '1234567890abcdefghigklmnopqrstuvyxwzABCDEFGHIGKLMNOPQRSTUVYXWZ'))  # Символы, из которых будет составлен пароль
        return pas
