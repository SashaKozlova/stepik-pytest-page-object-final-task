from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def register_new_user(self, email, password):
        login_input = self.browser.find_element(*LoginPageLocators.LOGIN_INPUT)
        login_input.send_keys(email)
        password1 = self.browser.find_element(*LoginPageLocators.PWD1_INPUT)
        password1.send_keys(password)
        password2 = self.browser.find_element(*LoginPageLocators.PWD2_INPUT)
        password2.send_keys(password)
        register = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        register.click()

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "URL does not contain login."

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented."

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented."
