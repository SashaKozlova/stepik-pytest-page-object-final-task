from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def should_be_promo_url(self):
        print(self.browser.current_url)
        assert "?promo=NewYear" in self.browser.current_url, "URL does not contain ?promo="

    def add_to_basket(self):
        button_add_to_basket = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        button_add_to_basket.click()

    def should_be_added_in_basket(self):
        message_product_added = self.browser.find_element(*ProductPageLocators.BOOK_ADDED).text
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        assert product_name == message_product_added,\
            "Name of the book: {product_name} does not mach with {message_product_added}."

    def should_be_basket_price(self):
        basket_price = self.browser.find_element(*ProductPageLocators.PRICE_BASKET).text
        product_price = self.browser.find_element(*ProductPageLocators.PRICE_BOOK).text
        print('check basket')
        assert product_price == basket_price, "Product price {product_price} not equal {basket_price}."

    def should_be_disappear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.BOOK_ADDED), \
            "Success message is presented, but should not be"

    def should_not_be_present_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"
