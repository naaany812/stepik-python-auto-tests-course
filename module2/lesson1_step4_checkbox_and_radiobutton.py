from selenium import webdriver
import time
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try: 
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)


    x = browser.find_element_by_css_selector('#input_value').text
    input_line = browser.find_element_by_css_selector('#answer').send_keys(calc(x))
    checkbox = browser.find_element_by_css_selector('label[for="robotCheckbox"]')
    checkbox.click()
    radiobutton = browser.find_element_by_css_selector('label[for="robotsRule"]')
    radiobutton.click()
    submit = browser.find_element_by_css_selector('button.btn[type="submit"]')
    submit.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()