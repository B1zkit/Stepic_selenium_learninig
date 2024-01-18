from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
    input1 = browser.find_element(By.NAME, "firstname")
    input1.send_keys("Vladimir")
    input2 = browser.find_element(By.NAME, "lastname")
    input2.send_keys("Afanasev")
    inpu3 = browser.find_element(By.NAME, "email")
    inpu3.send_keys("del@gmail.com")
    btn = browser.find_element(By.ID, "file")
    currentdir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(currentdir, "file.txt")
    btn.send_keys(file_path)
    sub = browser.find_element(By.CLASS_NAME, "btn")
    sub.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()