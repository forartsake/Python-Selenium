from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
LINK = "http://suninjuly.github.io/wait2.html"



try:
    with webdriver.Chrome() as browser:
        browser.get(LINK)
        button = WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.ID, "verify"))
        )
        button.click()
        message = browser.find_element(By.ID, "verify_message")

        assert "successful" in message.text
        time.sleep(5)
except Exception as error:
    print(f'An error was raised: {error}')

finally:
    print("Test has been closed.")
