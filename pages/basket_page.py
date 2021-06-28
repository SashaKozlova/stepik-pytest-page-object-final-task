from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def should_not_be_products(self):
        assert self.is_disappeared(*BasketPageLocators.ITEMS_BASKET)

    def should_be_text_empty_basket(self):
        text_empty_basket = "Your basket is empty. Continue shopping"
        content_basket = self.browser.find_element(*BasketPageLocators.CONTENT_BASKET).text
        print(content_basket)
        assert content_basket == text_empty_basket, "The basket isn't empty."
        assert self.is_element_present(*BasketPageLocators.CONTENT_BASKET)
