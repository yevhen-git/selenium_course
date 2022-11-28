from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_basket_page(self):
        self.should_be_empty_basket_url()

    def should_be_empty_basket_url(self):
        assert "basket" in self.browser.current_url,  "Basket url is incorrect"

    def should_be_empty_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), "Basket is not empty"

    def should_be_empty_text(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY_TEXT), "Basket is empty text is not presented"
