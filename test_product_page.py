import time
import pytest

from pages.base_page import BasePage
from pages.basket_page import BasketPage
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.main_page import MainPage
from pages.locators import MainPageLocators


class TestLoginFromProductPage():

    def test_guest_should_see_login_link_on_product_page(self, browser):
        link = "https://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_login_link()

    @pytest.mark.need_review
    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        link = "https://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.go_to_login_page()


class TestGuestTogetherWithTheProduct():
    @pytest.mark.need_review
    @pytest.mark.parametrize('link',
                             ["https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                              "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                              "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                              "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                              "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                              "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                              "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                              pytest.param(
                                  "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                                  marks=pytest.mark.xfail),
                              "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                              "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
    def test_guest_can_add_product_to_basket(self, browser, link):
        page = BasePage(browser, link)
        page.open()

        basket = ProductPage(browser, browser.current_url)
        basket.click_button_add_in_basket()
        basket.solve_quiz_and_get_code()
        basket.check_message_on_product_page()

    @pytest.mark.need_review
    def test_guest_cant_see_product_in_basket_opened_from_main_page(self, browser):
        link = "https://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.go_to_basket_page()
        basket_page = BasketPage(browser, browser.current_url)
        basket_page.check_empty_basket()


@pytest.mark.need_review
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
        page = BasePage(browser, link)
        time.sleep(5)
        page.open()
        log_page = LoginPage(browser, browser.current_url)
        log_page.go_to_login_page()
        log_page.register_new_user(page.generate_email(), page.generate_password())
        page.should_be_authorized_user()

    @pytest.mark.parametrize('link',
                             ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"])
    def test_user_cant_see_success_message_after_logged(self, browser, link):
        page = BasePage(browser, link)
        page.open()
        page.should_be_authorized_user()
        page.cant_see_success_message()

    @pytest.mark.parametrize('link',
                             ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"])
    def test_user_can_add_product_to_basket(self, browser, link):
        page = BasePage(browser, link)
        page.open()
        page.should_be_authorized_user()
        basket = ProductPage(browser, browser.current_url)
        basket.click_button_add_in_basket()
        basket.solve_quiz_and_get_code()
        basket.check_message_on_product_page()
