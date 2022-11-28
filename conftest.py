from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import pytest


def pytest_addoption(parser):
    parser.addoption('--language', default=None,
                     help="Choose language")


@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")

    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})

    browser = webdriver.Chrome(options=options)
    print(f"\nstart chrome browser for test in {user_language}...")
    yield browser
    print("\nquit browser..")
    browser.quit()
