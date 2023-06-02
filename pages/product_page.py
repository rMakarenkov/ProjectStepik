import math
import time
import credentials

from pages.base_page import BasePage
from pages.locators import MainPageLocators
from selenium.common.exceptions import NoAlertPresentException


class ProductPage(BasePage):

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

    def check_message_on_product_page(self):
        # проверяем, появилось ли сообщение с ценой товара в корзине
        assert self.is_element_present(*MainPageLocators.MESSAGE_PRICE_PRODUCT_LINK), "No such element"
        assert self.is_element_present(
            *MainPageLocators.MESSAGE_TO_ADD_PRODUCT_IN_BASKET_LINK), "Missing message to add item to basket"

        price = self.is_element_present_text(*MainPageLocators.PRICE_PRODUCT_LINK)
        price_message = self.is_element_present_text(*MainPageLocators.MESSAGE_PRICE_PRODUCT_LINK)
        name_item = self.is_element_present_text(*MainPageLocators.NAME_PRODUCT_LINK)
        product_message = self.is_element_present_text(*MainPageLocators.MESSAGE_TO_ADD_PRODUCT_IN_BASKET_LINK)

        # проверяем, что цена продукта фигурирует в сообщении
        assert price in price_message, "Price not in message"
        print(
            "The message contains the actual price of the product. The cost of the basket is the same as the price of the product: "
            f"\n {price.encode('utf-8')} "
            f"\n {price_message.encode('utf-8')}")

        # проверяем, что название продукта фигурирует в сообщении
        assert name_item in product_message, "Product not in message"
        print("The product name in the message matches the product that was added: "
              f"\n {name_item.encode('utf-8')} "
              f"\n {product_message.encode('utf-8')}")

        # проверяем, что сообщения соответствую эталонным. Предполагаем, что мы знаем практику формирования инфомрационных сообщений
        assert (credentials.REF_MESSAGE_TO_OUTPUT_PRICE + " " + price) == price_message, "Incorrectly formed message with the price of the product"
        assert (name_item + " " + credentials.REF_MESSAGE_TO_OUTPUT_NAME_ITEM) == product_message, "Incorrectly formed message with the name of the product"



