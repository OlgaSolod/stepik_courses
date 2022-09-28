import math

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    # говорим WebDriver ждать все элементы в течение 5 секунд
    browser.implicitly_wait(5)

    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), '$100'))
    btn = browser.find_element(By.ID, "book")
    btn.click()

    x = browser.find_element(By.ID, "input_value")
    value = calc(x.text)

    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(value)

    btn = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
    btn.click()
finally:
    time.sleep(10)
    browser.quit
