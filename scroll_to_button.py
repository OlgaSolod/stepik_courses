from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)


    value = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = value.text

    answer = browser.find_element(By.CSS_SELECTOR, "#answer")
    answer.send_keys(x)

    button = browser.find_element(By.CSS_SELECTOR, '[type="submit"')
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
finally:
    time.sleep(30)
    browser.quit