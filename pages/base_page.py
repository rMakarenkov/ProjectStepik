from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException

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

