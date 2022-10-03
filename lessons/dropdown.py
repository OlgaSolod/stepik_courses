from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.common.by import By
import time



link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)


    num1 = (browser.find_element(By.CSS_SELECTOR, "#num1")).text
    num2 = (browser.find_element(By.CSS_SELECTOR, "#num2")).text
    sum = int(num1) + int(num2)

    select = Select(browser.find_element(By.CSS_SELECTOR, "#dropdown"))
    select.select_by_value(str(sum))

    button = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
    button.click()
finally:
    time.sleep(30)
    browser.quit()



