import time

from pages.main_page import MainPage
from pages.login_page import LoginPage


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр
                                    # драйвера и url адрес
    page.open()  # открываем страницу
    page.go_to_login_page()  # выполняем метод страницы — переходим на страницу логина
    time.sleep(5)
    page.should_be_login_link()

    link_reg_auth = "http://selenium1py.pythonanywhere.com/ru/accounts/login"
    page_reg_auth = LoginPage(browser, link_reg_auth)
    page_reg_auth.should_be_login_page()

