from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

    BASKET_LINK = (By.CSS_SELECTOR, "a[class='btn btn-default']")

    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

    # для задачи по добавлению товара в корзину
    ADD_TO_BASKET_BUTTON_LINK = (By.CSS_SELECTOR, "#add_to_basket_form > button")

    MESSAGE_TO_ADD_PRODUCT_IN_BASKET_LINK = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div")

    MESSAGE_PRICE_PRODUCT_LINK = (
    By.CSS_SELECTOR, "#messages > div.alert.alert-safe.alert-noicon.alert-info.fade.in > div > p:nth-child(1)")

    PRICE_PRODUCT_LINK = (By.CSS_SELECTOR, "#content_inner > article > div.row "
                                           "> div.col-sm-6.product_main > p.price_color")

    NAME_PRODUCT_LINK = (By.CSS_SELECTOR, "#content_inner > article > div.row > div.col-sm-6.product_main > h1")


class LoginPageLocators():
    LOGIN_FORM_LINK = (By.CSS_SELECTOR, "#login_form")

    REGISTER_FORM_LINK = (By.CSS_SELECTOR, "#register_form")

    EMAIL_INPUT_LINK = (By.CSS_SELECTOR, "#id_registration-email")

    PASS_INPUT_LINK = (By.CSS_SELECTOR, "#id_registration-password1")

    DOUBLE_PASS_INPUT_LINK = (By.CSS_SELECTOR, "#id_registration-password2")

    BUTTON_REG_NEW_USER = (By.CSS_SELECTOR, "button[value='Register']")


class BasketPageLocators():
    BASKET_EMPTY_LINK = (By.CSS_SELECTOR, "#content_inner > p")

    BUTTON_PROTECTED_TO_CHECKOUT_LINK = (By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-block")
