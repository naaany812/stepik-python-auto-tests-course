from selenium import webdriver
import time

try: 
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    #first_name = browser.find_element_by_css_selector('input[placeholder="Input your first name"]')
    #first_name.send_keys("Ivan")
    #last_name = browser.find_element_by_css_selector('input[placeholder="Input your last name"]')
    #last_name.send_keys("Ivanov")
    #email = browser.find_element_by_css_selector('input[placeholder="Input your email"]')
    #email.send_keys("ivan.ivanov@ivan.com")
    #phone = browser.find_element_by_css_selector('input[placeholder="Input your phone:"]')
    #phone.send_keys("89214480977")
    #address = browser.find_element_by_css_selector('input[placeholder="Input your address:"]')
    #address.send_keys("Address maza faka")
    
    first_name = browser.find_element_by_css_selector('div.first_block input.first')
    first_name.send_keys("Ivan")
    last_name = browser.find_element_by_css_selector('div.first_block input.second')
    last_name.send_keys("Ivanov")
    email = browser.find_element_by_css_selector('div.first_block input.third')
    email.send_keys("ivan.ivanov@ivan.com")
    phone = browser.find_element_by_css_selector('div.second_block input.first')
    phone.send_keys("89214480977")
    address = browser.find_element_by_css_selector('div.second_block input.second')
    address.send_keys("Address maza faka")

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()