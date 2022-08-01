from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

FILE_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'file.txt')
LINK = "http://suninjuly.github.io/file_input.html"
DATA = {'firstname': "John",
        'lastname': "Smith",
        'email': "john2smith@gmail.com"
        }

try:
    with webdriver.Chrome() as browser:
        browser.get(LINK)
        for name, value in DATA.items():
            browser.find_element(By.NAME, name).send_keys(value)
        browser.find_element(By.ID, 'file').send_keys(FILE_PATH)
        browser.find_element(By.CSS_SELECTOR, 'button.btn').click()
        time.sleep(5)
except Exception as error:
    print(f'An error was raised: {error}')

finally:
    print("Test has been closed.")
