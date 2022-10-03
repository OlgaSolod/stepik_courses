import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


link = "http://suninjuly.github.io/file_input.html"


try:
    browser = webdriver.Chrome()
    browser.get(link)

    first_name = browser.find_element(By.NAME, "firstname")
    first_name.send_keys("Кот")

    last_name = browser.find_element(By.NAME, "lastname")
    last_name.send_keys("Бесфамильный")

    email = browser.find_element(By.NAME, "email")
    email.send_keys("cat@cat.ru")

    file = browser.find_element(By.CSS_SELECTOR, '[type="file"]')
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    file.send_keys(file_path)

    btn = browser. find_element(By.CSS_SELECTOR, '[type="submit"]')
    btn.click()

finally:
    time.sleep(30)
    browser.quit()

