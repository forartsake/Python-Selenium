from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/simple_form_find_task.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.TAG_NAME, "input")
    input1.send_keys("John")
    input2 = browser.find_element(By.NAME, 'last_name')
    input2.send_keys("Smith")
    input3 = browser.find_element(By.CLASS_NAME, 'form-control.city')
    input3.send_keys("Glasgow")
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Scotland")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # time.sleep(30)
    browser.quit()