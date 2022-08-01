from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

LINK = "http://suninjuly.github.io/explicit_wait2.html"

def calc(value):
    return math.log((abs(12*math.sin(value))))

try:
    with webdriver.Chrome() as browser:
        browser.get(LINK)
        price = WebDriverWait(browser, 12).until(
            EC.text_to_be_present_in_element((By.ID, 'price'), '100')
        )
        browser.find_element(By.ID, 'book').click()
        browser.execute_script('window.scrollBy(0, 300);')
        browser.find_element(By.ID, 'answer').send_keys(
            calc(int(browser.find_element(By.ID, 'input_value').text))
        )
        browser.find_element(By.ID, 'solve').click()

        time.sleep(5)
except Exception as error:
    print(f'An error was raised: {error}')

finally:
    print("Test has been closed.")
