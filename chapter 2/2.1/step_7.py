from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc_fun(data):
    return str(math.log(abs(12*math.sin(int(data)))))

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    with webdriver.Chrome() as browser:
        browser.get(link)
        find_value = browser.find_element(By.ID, 'treasure')
        value = find_value.get_attribute("valuex")
        calc_value = calc_fun(value)
        input1 = browser.find_element(By.ID, 'answer')
        input1.send_keys(calc_value)
        input2 = browser.find_element(By.ID, 'robotCheckbox')
        input2.click()
        input3 = browser.find_element(By.ID, 'robotsRule')
        input3.click()
        button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
        button.click()
        time.sleep(5)


finally:
    print("Test has been closed")