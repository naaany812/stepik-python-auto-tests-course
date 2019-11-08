from selenium import webdriver
import os
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/file_input.html")
    browser.find_element_by_name("firstname").send_keys("Annet")
    browser.find_element_by_name("lastname").send_keys("Ivanova")
    browser.find_element_by_name("email").send_keys("Annet.Ivanova@tester.com")
    current_folder = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_folder, "file.txt")
    browser.find_element_by_id("file").send_keys(file_path)
    browser.find_element_by_tag_name("button").click()
finally:
    time.wait(5)
    browser.close()
