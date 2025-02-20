from selenium import webdriver
from selenium.webdriver.common.by import By
import time

###
### STEP 7
###

import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "https://suninjuly.github.io/get_attribute.html"

    browser = webdriver.Chrome()
    browser.get(link)

    treasureEl = browser.find_element(By.CSS_SELECTOR, "#treasure")

    x = treasureEl.get_attribute("valuex")
    y = calc(x)

    entry = browser.find_element(By.CSS_SELECTOR, "#answer")
    entry.send_keys(y)

    check = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    check.click()

    radioEl = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    radioEl.click()

    sumbitBt = browser.find_element(By.CSS_SELECTOR, "body > div > form > div > div > button")
    sumbitBt.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
