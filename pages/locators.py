from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    LOGIN_INPUT = (By.CSS_SELECTOR, "#id_registration-email")
    PWD1_INPUT = (By.CSS_SELECTOR, "#id_registration-password1")
    PWD2_INPUT = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "#register_form > button")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-succes")


class ProductPageLocators:
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    BOOK_ADDED = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main > h1")
    PRICE_BOOK = (By.CSS_SELECTOR, ".product_main > p.price_color")
    PRICE_BASKET = (By.CSS_SELECTOR, "div.alertinner > p:nth-child(1) > strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(1)")


class BasketPageLocators:
    BUTTON_BASKET = (By.CSS_SELECTOR, ".basket-mini > span > a")
    CONTENT_BASKET = (By.CSS_SELECTOR, "#content_inner > p")
    ITEMS_BASKET = (By.CSS_SELECTOR, "#basket_formset")
