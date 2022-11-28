import pytest
from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
import time


@pytest.mark.new
class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        # открыть страницу регистрации;
        register_link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
        login_page = LoginPage(browser, register_link)
        login_page.open()
        email = str(time.time()) + "@fakemail.org"
        # зарегистрировать нового пользователя;
        login_page.register_new_user(email, 'Ukraine123')
        login_page.should_be_authorized_user()

    def test_user_cant_see_success_message_after_adding_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        page.add_to_cart()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
        # initiate Page Object, send construction of driver and url
        page = ProductPage(browser, link)
        page.open()
        page.add_to_cart()
        page.solve_quiz_and_get_code()
        page.should_be_message_about_adding()
        page.should_be_message_basket_total()


def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_cart()
    page.should_dissapear_success_message()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = ProductPage(browser, link)
    page.open()
    # Переходит в корзину по кнопке в шапке сайта
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_basket_page()
    # Ожидаем, что в корзине нет товаров
    basket_page.should_be_empty_basket()
    # Ожидаем, что есть текст о том что корзина пуста
    basket_page.should_be_empty_text()


def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_cart()
    page.should_not_be_success_message()


@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    # initiate Page Object, send construction of driver and url
    page = ProductPage(browser, link)
    page.open()
    page.add_to_cart()
    page.solve_quiz_and_get_code()
    page.should_be_message_about_adding()
    page.should_be_message_basket_total()