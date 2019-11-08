import time

from selenium import webdriver
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/execute_script.html")
    x = browser.find_element_by_id("input_value").text
    browser.execute_script("window.scrollBy(0, 100);")
    browser.find_element_by_id("answer").send_keys(calc(x))
    for element in browser.find_elements_by_class_name("form-check-label"):
        element.click()
    browser.find_element_by_class_name("btn").click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

