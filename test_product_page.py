import pytest

from pages.product_page import ProductPage
from pages.main_page import MainPage
from pages.locators import MainPageLocators


@pytest.mark.login
class TestLoginFromProductPage():

    def test_guest_should_see_login_link_on_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_login_link()

    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.go_to_login_page()


class TestUserAddToBasketFromProductPage():
    @pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"])
    def test_guest_cant_see_success_message(self, browser, link):
        page = MainPage(browser, link)
        page.open()
        assert page.is_not_element_present(
            *MainPageLocators.MESSAGE_TO_ADD_PRODUCT_IN_BASKET_LINK), "The message is on the current page"
