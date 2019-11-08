from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import math
import time


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    button = browser.find_element_by_id("book")
    WebDriverWait(browser, 15).until(expected_conditions.text_to_be_present_in_element((By.ID, "price"), "$100"))
    button.click()
    x = browser.find_element_by_id("input_value").text
    browser.find_element_by_tag_name("input").send_keys(calc(x))
    browser.find_element_by_id("solve").click()
finally:
    time.sleep(5)
    browser.close()

