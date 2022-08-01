from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc_fun(data):
    return str(math.log(abs(12*math.sin(int(data)))))

try:
    link = "https://suninjuly.github.io/math.html"
    with webdriver.Chrome() as browser:
        browser.get(link)

        data_el = browser.find_element(By.ID, 'input_value')
        value = data_el.text
        calc_value = calc_fun(value)
        answer = browser.find_element(By.ID, 'answer')
        answer.send_keys(calc_value)

        checkbox = browser.find_element(By.ID, 'robotCheckbox')
        checkbox.click()
        radiobutton = browser.find_element(By.ID, 'robotsRule')
        radiobutton.click()

        submit = browser.find_element(By.CSS_SELECTOR, 'button.btn')
        submit.click()
        time.sleep(10)

finally:
    print("Test has been closed ")
