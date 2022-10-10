from email.policy import default
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.options import Options


browser = webdriver.Chrome(options=options)


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default=None, help='Choose browser: chrome or firefox')
    parser.addoption('--browser_name', action='store', default=None, help='Choose language: en or ru')

@pytest.fixture
def browser(request):
    
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption('language')
    browser = None
    if browser_name == 'chrome' and language:
        print("\nstart chrome browser for test..")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome()
    elif browser_name == 'firefox':
        print('\nstart firefox browser for test...')
        browser = webdriver.Firefox()
    else:
        raise pytest.UsageError('--browser_name should be chrome or firefox')
    yield browser
    print("\nquit browser..")
    browser.quit()