from selenium import webdriver
import time


try: 
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    
    num1 = browser.find_element_by_id('num1').text
    num2 = browser.find_element_by_id('num2').text
    select_dropdown = webdriver.support.ui.Select(browser.find_element_by_id('dropdown'))
    select_dropdown.select_by_visible_text(str(int(num1) + int(num2)))
    submit = browser.find_element_by_css_selector('button.btn[type="submit"]')
    submit.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()