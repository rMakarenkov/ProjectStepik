import pytest

from pages.main_page import MainPage
from pages.test_product_page import BasketPage

def test_ca_add_product_in_bascket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    link2 = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = MainPage(browser, link2)
    page.open()

    basket = BasketPage(browser, browser.current_url)
    basket.click_button_add_in_basket()
    basket.solve_quiz_and_get_code()
    basket.check_message_on_main_page()



