import unittest
import time
from selenium.webdriver.common.by import By
from selenium import webdriver




class SearchSelectors(unittest.TestCase):
    def test_registration1(self):
        link = "http://suninjuly.github.io/registration1.html"
        # text = test_steps(link)
        browser = webdriver.Chrome()
        browser.get(link)
        input1 = browser.find_element(By.CSS_SELECTOR, '.first_block>div.first_class>input')
        input1.send_keys('Name')

        input2 = browser.find_element(By.CSS_SELECTOR, '.first_block>div.second_class>input')
        input2.send_keys('Surname')
                
        input3 = browser.find_element(By.CSS_SELECTOR, '.first_block>div.third_class>input')
        input3.send_keys('email')


        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Text doesn't coincide" )

    def test_registration2(self):
        link = "http://suninjuly.github.io/registration2.html"
        # text = test_steps(link)
        browser = webdriver.Chrome()
        browser.get(link)
        input1 = browser.find_element(By.CSS_SELECTOR, '.first_block>div.first_class>input')
        input1.send_keys('Name')

        input2 = browser.find_element(By.CSS_SELECTOR, '.first_block>div.second_class>input')
        input2.send_keys('Surname')
                
        input3 = browser.find_element(By.CSS_SELECTOR, '.first_block>div.third_class>input')
        input3.send_keys('email')


        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Text doesn't coincide" )
    
# def test_steps(link):
    # browser = webdriver.Chrome()
    # browser.get(link)
    # input1 = browser.find_element(By.CSS_SELECTOR, '.first_block>div.first_class>input')
    # input1.send_keys('Name')

    # input2 = browser.find_element(By.CSS_SELECTOR, '.first_block>div.second_class>input')
    # input2.send_keys('Surname')
            
    # input3 = browser.find_element(By.CSS_SELECTOR, '.first_block>div.third_class>input')
    # input3.send_keys('email')


    # # Отправляем заполненную форму
    # button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    # button.click()

    # # Проверяем, что смогли зарегистрироваться
    # # ждем загрузки страницы
    # time.sleep(1)

    # # находим элемент, содержащий текст
    # welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # # записываем в переменную welcome_text текст из элемента welcome_text_elt
    # welcome_text = welcome_text_elt.text
    # return welcome_text
if __name__ == "__main__":
    unittest.main()