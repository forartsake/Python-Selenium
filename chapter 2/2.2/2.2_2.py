import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
from selenium.webdriver.common.keys import Keys

def calc(value):
    return math.log((abs(12*math.sin(int(value)))))



try:

    link = "https://suninjuly.github.io/execute_script.html"
    with webdriver.Chrome() as browser:
        browser.get(link)
        value = browser.find_element(By.ID, 'input_value').text
        input1 = browser.find_element(By.ID, 'answer').send_keys(calc(value))

        browser.execute_script("window.scrollBy(0, 150);")

        browser.find_element(By.ID, 'robotCheckbox').click()
        browser.find_element(By.ID, 'robotsRule').click()

        button = browser.find_element(By.TAG_NAME, 'button').submit()
        time.sleep(3)

except Exception as error:
    print(f'Error description: {error}')

finally:
    print("Test has been closed")
