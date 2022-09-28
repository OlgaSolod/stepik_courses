from selenium import webdriver
from selenium.webdriver.common.by import By

link = "https://litecart.stqa.ru/en/"
try:
    browser = webdriver.Chrome()
    browser.get(link)
    browser.implicitly_wait(5)


    elements = browser.find_elements(By.XPATH, "//div[@class='content']//ul/li[contains(@class, 'product')]")
    for i in elements:
        print(i.text)
finally:
    browser.quit()