from selenium import webdriver
import math
import time


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/alert_accept.html")
    browser.find_element_by_tag_name("button").click()
    alert = browser.switch_to.alert
    alert.accept()
    x = browser.find_element_by_id("input_value").text
    browser.find_element_by_tag_name("input").send_keys(calc(x))
    browser.find_element_by_tag_name("button").click()

finally:
    time.sleep(5)
    browser.close()