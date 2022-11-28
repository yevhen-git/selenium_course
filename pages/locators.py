from selenium.webdriver.common.by import By


class BasePageLocators:
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    # LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    VIEW_BASKET_LINK = (By.CSS_SELECTOR, "span a[href*='basket']")


class LoginPageLocators:
    login_form = (By.CSS_SELECTOR, "form#login_form")
    email_login = (By.CSS_SELECTOR, "input#id_login-username")
    password_login = (By.CSS_SELECTOR, "input#id_login-password")
    forgot_link = (By.CSS_SELECTOR, "#login_form p a")
    button_login = (By.CSS_SELECTOR, "button[name=login_submit]")

    registration_form = (By.CSS_SELECTOR, "form#register_form")
    EMAIL_REGISTRATION = (By.CSS_SELECTOR, "input#id_registration-email")
    PASSWORD_REGISTRATION = (By.CSS_SELECTOR, "input#id_registration-password1")
    PASSWORD_CONFIRM = (By.CSS_SELECTOR, "input#id_registration-password2")
    BUTTON_REGISTER = (By.CSS_SELECTOR, "button[name=registration_submit]")


class ProductPageLocators:
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "button[class='btn btn-lg btn-primary btn-add-to-basket']")
    MESSAGE_ABOUT_ADDING = (By.CSS_SELECTOR, "div.alertinner strong")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main h1")
    MESSAGE_BASKET_TOTAL = (By.CSS_SELECTOR, ".alert-info .alertinner strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")


class BasketPageLocators:
    BASKET_ITEMS = (By.CSS_SELECTOR, "div.basket-items")
    BASKET_EMPTY_TEXT = (By.XPATH, "//p[contains(text(), 'Your basket is empty.')]")
