from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x = browser.find_element(By.ID, "num1").text
    y = browser.find_element(By.ID, "num2").text
    res = int(x) + int(y)
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_visible_text(str(res))
    btn = browser.find_element(By.CLASS_NAME, "btn")
    btn.click()
    browser.execute_script("alert('Robots at work');")

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()