from selenium import webdriver
import time
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try: 
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)


    x = browser.find_element_by_css_selector('#treasure').get_attribute("valuex")
    input_line = browser.find_element_by_css_selector('#answer').send_keys(calc(x))
    checkbox = browser.find_element_by_css_selector('#robotCheckbox')
    checkbox.click()
    radiobutton = browser.find_element_by_css_selector('#robotsRule')
    radiobutton.click()
    submit = browser.find_element_by_css_selector('button.btn[type="submit"]')
    submit.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()