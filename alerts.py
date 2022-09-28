from selenium.webdriver.common.by import By
from selenium import webdriver
import time
import math


link = 'http://suninjuly.github.io/alert_accept.html'


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get(link)

    btn = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    btn.click()

    confirm = browser.switch_to.alert.accept()

    x = browser.find_element(By.ID, "input_value")
    value = calc(x.text)

    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(value)

    sbm_btn = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    sbm_btn.click()
finally:
    time.sleep(30)
    browser.quit()
