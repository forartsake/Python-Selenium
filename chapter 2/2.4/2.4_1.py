from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
import math

LINK = "http://suninjuly.github.io/wait1.html"



try:
    with webdriver.Chrome() as browser:
        browser.get(LINK)
        browser.implicitly_wait(5)
        button = browser.find_element(By.ID, "verify")
        button.click()
        message = browser.find_element(By.ID, "verify_message")

        assert "successful" in message.text

        time.sleep(5)
except Exception as error:
    print(f'An error was raised: {error}')

finally:
    print("Test has been closed.")
