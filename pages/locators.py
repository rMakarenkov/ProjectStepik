from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

    # для задачи по добавлению товара в корзину
    ADD_TO_BASKET_BUTTON_LINK = (By.CSS_SELECTOR, "#add_to_basket_form > button")

    MESSAGE_TO_ADD_PRODUCT_IN_BASKET_LINK = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div")

    MESSAGE_PRICE_PRODUCT_LINK = (By.CSS_SELECTOR, "#messages > div.alert.alert-safe.alert-noicon.alert-info.fade.in > div > p:nth-child(1)")

    PRICE_PRODUCT_LINK = (By.CSS_SELECTOR, "#content_inner > article > div.row "
                                           "> div.col-sm-6.product_main > p.price_color")

    NAME_PRODUCT_LINK = (By.CSS_SELECTOR, "#content_inner > article > div.row > div.col-sm-6.product_main > h1")

class LoginPageLocators():
    LOGIN_FORM_LINK = (By.CSS_SELECTOR, "#login_form")

    REGISTER_FORM_LINK = (By.CSS_SELECTOR, "#register_form")

#class BasketPageLocators():

