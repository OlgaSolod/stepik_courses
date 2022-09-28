from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/get_attribute.html"

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    field = browser.find_element(By.CSS_SELECTOR, "#answer")
    x_element = browser.find_element(By.CSS_SELECTOR, "#treasure")
    x_attr = x_element.get_attribute("valuex")
    print(x_attr)
    y = calc(x_attr)
    field.send_keys(y)

    checkbox = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    checkbox.click()

    radiobutton = browser.find_element(By.CSS_SELECTOR, '#robotsRule')
    radiobutton.click()

    time.sleep(1)
    button = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
    button.click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

