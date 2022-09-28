from selenium.webdriver.common.by import By
from selenium import webdriver
import math
import time

link = "http://suninjuly.github.io/redirect_accept.html"


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get(link)

    btn = browser.find_element(By.CSS_SELECTOR, ".trollface.btn-primary")
    btn.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    field = browser.find_element(By.CSS_SELECTOR, "#answer")
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)
    field.send_keys(y)

    button = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
    button.click()
finally:
    time.sleep(30)
    browser.quit()