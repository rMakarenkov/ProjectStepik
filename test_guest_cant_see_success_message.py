import pytest
import time

from pages.main_page import MainPage
from pages.product_page import ProductPage
from pages.locators import MainPageLocators

@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"])
def test_guest_cant_see_success_message(browser, link):
    page = MainPage(browser, link)
    page.open()
    assert page.is_not_element_present(*MainPageLocators.MESSAGE_TO_ADD_PRODUCT_IN_BASKET_LINK), "The message is on the current page"







