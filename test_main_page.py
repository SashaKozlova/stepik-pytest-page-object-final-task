from pages.main_page import BasePage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage
import pytest


@pytest.mark.login_guest
class TestLoginFromMainPage:
    def test_guest_can_go_to_login_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = BasePage(browser, link)
        page.open()
        page.go_to_login_page()
        page1 = LoginPage(browser, page.browser.current_url)
        page1.should_be_login_page()

    def test_guest_should_see_login_link(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = BasePage(browser, link)
        page.open()
        page.should_be_login_link()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = BasePage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, page.browser.current_url)
    basket_page.should_not_be_products()
    basket_page.should_be_text_empty_basket()
