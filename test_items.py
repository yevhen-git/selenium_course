from selenium.webdriver.common.by import By
import time


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_user_should_see_add_to_basket_button(browser):
    browser.get(link)
    time.sleep(10)
    ADD_BASKET_BUTTON = browser.find_elements(By.CSS_SELECTOR, "form#addsdsd_to_basket_form button")
    assert ADD_BASKET_BUTTON,  "'Add to Basket' button is not displayed on the page"
