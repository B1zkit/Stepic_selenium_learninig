from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x = browser.find_element(By.ID, "treasure").get_attribute("valuex")
    y = calc(x)
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)
    chckX = browser.find_element(By.ID, "robotCheckbox")
    chckX.click()
    rad = browser.find_element(By.ID, "robotsRule")
    rad.click()
    but = browser.find_element(By.CLASS_NAME, "btn")
    but.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()