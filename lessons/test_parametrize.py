import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait  
import time
import math


test_links = [
    'https://stepik.org/lesson/236895/step/1',
    'https://stepik.org/lesson/236896/step/1',
    'https://stepik.org/lesson/236897/step/1',
    'https://stepik.org/lesson/236898/step/1',
    'https://stepik.org/lesson/236899/step/1',
    'https://stepik.org/lesson/236903/step/1',
    'https://stepik.org/lesson/236904/step/1',
    'https://stepik.org/lesson/236905/step/1'
]


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(10)
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('link', test_links)
def test_answer_is_correct(browser, link):
    browser.get(link)
    answer = math.log(int(time.time()))
    field_answer = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.ember-text-area.ember-view.textarea.string-quiz__textarea')))
    field_answer.send_keys(answer)
    submit_btn = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.submit-submission')))
    submit_btn.click()
    feedback = browser.find_element(By.CSS_SELECTOR, '.smart-hints__hint')
    assert feedback.text == 'Correct!', 'Text in feedback doesn\'t match'

    
