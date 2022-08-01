from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
import math

LINK = "http://suninjuly.github.io/redirect_accept.html"


def calc(value: int):
    return math.log(abs(12*math.sin(value)))


try:
    with webdriver.Chrome() as browser:
        browser.get(LINK)
        browser.find_element(By.CSS_SELECTOR, 'button.btn').click()
        windows = browser.window_handles
        browser.switch_to.window(windows[1])
        browser.find_element(By.ID, 'answer').send_keys(calc(int(browser.find_element(By.ID, 'input_value').text)))
        browser.find_element(By.CSS_SELECTOR, 'button.btn').click()



        time.sleep(5)
except Exception as error:
    print(f'An error was raised: {error}')

finally:
    print("Test has been closed.")
