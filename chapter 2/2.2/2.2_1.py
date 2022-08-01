from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

try:

    link = "http://suninjuly.github.io/selects1.html"
    with webdriver.Chrome() as browser:
        browser.get(link)

        num1 = int(browser.find_element(By.ID, 'num1').text)
        num2 = int(browser.find_element(By.ID, 'num2').text)

        select = Select(browser.find_element(By.TAG_NAME, 'select'))
        select.select_by_value(str(num1 + num2))

        button = browser.find_element(By.CSS_SELECTOR, 'button.btn').click()

        time.sleep(5)

except Exception as error:
    print(f'Error description: {error}')

finally:
    print("Test has been closed")
