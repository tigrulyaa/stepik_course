from selenium import webdriver
from selenium.webdriver.common.by import By
import time

###
### STEP 8
###

import os 


try:
    link = "https://suninjuly.github.io/file_input.html"

    browser = webdriver.Chrome()
    browser.get(link)

    firstName = browser.find_element(By.CSS_SELECTOR, "body > div > form > div > input:nth-child(2)")
    firstName.send_keys('Name')

    lastName = browser.find_element(By.CSS_SELECTOR, "body > div > form > div > input:nth-child(4)")
    lastName.send_keys('LastName')

    email = browser.find_element(By.CSS_SELECTOR, "body > div > form > div > input:nth-child(6)")
    email.send_keys('email')

    element = browser.find_element(By.CSS_SELECTOR, "#file")
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'meow.jpg')           # добавляем к этому пути имя файла \
    element.send_keys(file_path)

    sumbitBt = browser.find_element(By.CSS_SELECTOR, "body > div > form > button")
    sumbitBt.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

