from pages.base_page import BasePage
from pages.locators import MainPageLocators
from .login_page import LoginPage
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException


class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)