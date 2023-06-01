import math
import time

from pages.base_page import BasePage
from pages.locators import MainPageLocators
from selenium.common.exceptions import NoAlertPresentException


class BasketPage(BasePage):

    def click_button_add_in_basket(self):
        button_in_basket = self.browser.find_element(*MainPageLocators.ADD_TO_BASKET_BUTTON_LINK)
        button_in_basket.click()

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
            time.sleep(10)
        except NoAlertPresentException:
            print("No second alert presented")

    def check_message_on_main_page(self):
        # проверяем, появилось ли сообщение с ценой товара в корзине
        assert self.is_element_present(*MainPageLocators.MESSAGE_PRICE_PRODUCT_LINK), "No such element"
        assert self.is_element_present(*MainPageLocators.MESSAGE_TO_ADD_PRODUCT_IN_BASKET_LINK), "Missing message to add item to basket"

        price = self.is_element_present_text(*MainPageLocators.PRICE_PRODUCT_LINK)
        price_in_message = self.is_element_present_text(*MainPageLocators.MESSAGE_PRICE_PRODUCT_LINK)
        name_product = self.is_element_present_text(*MainPageLocators.NAME_PRODUCT_LINK)
        product_in_message = self.is_element_present_text(*MainPageLocators.MESSAGE_TO_ADD_PRODUCT_IN_BASKET_LINK)

        assert price in price_in_message, "Price not in message"
        print("В сообщении находится действительная цена продукта. Стоимость корзины совпадает с ценой продукта: "
              f"\n {price.encode('utf-8')} "
              f"\n {price_in_message.encode('utf-8')}")
        assert name_product in product_in_message, "Product not in message"
        print("Название товара в сообщении совпадает с тем товаром, который был добавлен: "
              f"\n {name_product.encode('utf-8')} "
              f"\n {product_in_message.encode('utf-8')}")







