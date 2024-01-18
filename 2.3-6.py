from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    btn1 = browser.find_element(By.TAG_NAME, "button")
    btn1.click()
    second_window = browser.window_handles[1]
    browser.switch_to.window(second_window)
    x = browser.find_element(By.ID, "input_value").text
    y = calc(x)
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)
    btn2 = browser.find_element(By.CLASS_NAME, "btn")
    btn2.click()




finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()