import time
import pytest

from pages.base_page import BasePage
from pages.locators import MainPageLocators
from pages.login_page import LoginPage
from pages.basket_page import BasketPage
from pages.product_page import ProductPage


# def test_guest_can_go_to_login_page(browser):
#     link = "http://selenium1py.pythonanywhere.com/"
#     page = BasePage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр
#     # драйвера и url адрес
#     page.open()  # открываем страницу
#     page.go_to_login_page()  # выполняем метод страницы — переходим на страницу логина
#
#     login_page = LoginPage(browser, browser.current_url)
#     login_page.should_be_login_page()


@pytest.mark.login_guest
class TestLoginFromMainPage():
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
        page = BasePage(browser, link)
        time.sleep(5)
        page.open()

        log_page = LoginPage(browser, browser.current_url)
        log_page.go_to_login_page()
        log_page.register_new_user(page.generate_email(), page.generate_password())
        page.should_be_login_link()
    @pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"])
    def test_guest_cant_see_success_message(self, browser, link):
        page = BasePage(browser, link)
        page.open()
        page.should_be_login_link()
        assert page.is_not_element_present(
            *MainPageLocators.MESSAGE_TO_ADD_PRODUCT_IN_BASKET_LINK), "The message is on the current page"

    @pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"])
    def test_can_add_product_in_basket(self, browser, link):
        page = BasePage(browser, link)
        page.open()
        page.should_be_login_link()

        basket = ProductPage(browser, browser.current_url)
        basket.click_button_add_in_basket()
        basket.solve_quiz_and_get_code()
        basket.check_message_on_product_page()

