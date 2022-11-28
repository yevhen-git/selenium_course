from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_cart(self):
        add_to_cart_btn = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON)
        add_to_cart_btn.click()

    def should_be_message_about_adding(self):
        # Сначала проверяем, что элементы присутствуют на странице
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), (
            "Product name is not presented")
        assert self.is_element_present(*ProductPageLocators.MESSAGE_ABOUT_ADDING), (
            "Message about adding is not presented")
        # Затем получаем текст элементов для проверки
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        message = self.browser.find_element(*ProductPageLocators.MESSAGE_ABOUT_ADDING).text
        # Проверяем, что название товара присутствует в сообщении о добавлении
        assert product_name == message, f"No product name in the message, {product_name}, and {message}"

    def should_be_message_basket_total(self):
        # Сначала проверяем, что элементы присутствуют на странице
        assert self.is_element_present(*ProductPageLocators.MESSAGE_BASKET_TOTAL), (
            "Message basket total is not presented")
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE), (
            "Product price is not presented")
        # Затем получаем текст элементов для проверки
        message_basket_total = self.browser.find_element(*ProductPageLocators.MESSAGE_BASKET_TOTAL).text
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        # Проверяем, что цена товара присутствует в сообщении со стоимостью корзины
        assert product_price == message_basket_total, f"No product price in the message {product_price}, and {message_basket_total}"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.MESSAGE_ABOUT_ADDING), "Success message is presented, but should not be"

    def should_dissapear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.MESSAGE_ABOUT_ADDING), "Success message is presented, but should be dissapered"