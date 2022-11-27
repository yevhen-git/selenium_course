from selenium.webdriver.common.by import By


class LoginPageLocators:
    login_form = (By.CSS_SELECTOR, "form#login_form")
    email_login = (By.CSS_SELECTOR, "input#id_login-username")
    password_login = (By.CSS_SELECTOR, "input#id_login-password")
    forgot_link = (By.CSS_SELECTOR, "#login_form p a")
    button_login = (By.CSS_SELECTOR, "button[name=login_submit]")

    registration_form = (By.CSS_SELECTOR, "form#register_form")
    email_registration = (By.CSS_SELECTOR, "input#id_registration-email")
    password_registration = (By.CSS_SELECTOR, "input#id_registration-password1")
    password_confirm = (By.CSS_SELECTOR, "input#id_login-registration-password2")
    button_register = (By.CSS_SELECTOR, "button[name=registration_submit]")


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
