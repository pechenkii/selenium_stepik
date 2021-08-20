from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    # добавление товара в корзину
    def add_to_basket(self):
        add_btn = self.browser.find_element(*ProductPageLocators.BTN_ADD_BASKET)
        add_btn.click()

    def should_be_adding_message(self):
        # проверка, что есть сообщение о добавлении товара
        assert self.is_element_present(*ProductPageLocators.PRODUCT_IN_MESSAGE), "Product message is not presented"

    def should_be_product_in_message(self):
        # проверка на совпадение названия товара с названием в сообщении
        prod_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        message = self.browser.find_element(*ProductPageLocators.PRODUCT_IN_MESSAGE)
        assert prod_name.text == message.text, "Product name not in message"

    def product_price_equals_basket_price(self):
        prod_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        bask_price = self.browser.find_element(*ProductPageLocators.PRICE_BASKET)
        assert prod_price.text == bask_price.text, "Product price not equals basket price"