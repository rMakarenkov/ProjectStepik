import pytest
import time

from pages.main_page import MainPage
from pages.product_page import ProductPage
from pages.locators import MainPageLocators

@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"])
def test_message_disappeared_after_adding_product_to_basket(browser, link):
    page = MainPage(browser, link)
    page.open()
    basket = ProductPage(browser, browser.current_url)
    basket.click_button_add_in_basket()
    basket.check_message_on_product_page()
    assert page.is_disappeared(*MainPageLocators.MESSAGE_TO_ADD_PRODUCT_IN_BASKET_LINK), "The post didn't disappear from the page"







