from .base_page import BasePage
from .locators import LoginPageLocators
import time


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url,  "Login url is incorrect"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.login_form), "Login form is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.registration_form), "Register form is not presented"

    def register_new_user(self, email, password):
        email_register = self.browser.find_element(*LoginPageLocators.EMAIL_REGISTRATION)
        email_register.send_keys(email)
        password_field = self.browser.find_element(*LoginPageLocators.PASSWORD_REGISTRATION)
        confirm_password = self.browser.find_element(*LoginPageLocators.PASSWORD_CONFIRM)
        password_field.send_keys(password)
        confirm_password.send_keys(password)
        register_btn = self.browser.find_element(*LoginPageLocators.BUTTON_REGISTER)
        register_btn.click()
