from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import pytest


@pytest.fixture(scope="function")
def browser():
    chrome_options = Options()
    chrome_options.add_argument("--headless")

    browser = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=chrome_options)
    # чтоб браузер запускался в фоне
    # browser = webdriver.Chrome(options=chrome_options)

    print(f"\nstart chrome browser...")
    yield browser
    print("\nquit browser..")
    browser.quit()
