from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/find_link_text"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    find_link = browser.find_element(By.PARTIAL_LINK_TEXT, str(math.ceil(math.pow(math.pi, math.e)*10000)))
    find_link.click()
    input1 = browser.find_element(By.NAME, "first_name")
    input1.send_keys('John')
    input2 = browser.find_element(By.NAME, "last_name")
    input2.send_keys('Smith')
    input3 = browser.find_element(By.CLASS_NAME, 'form-control.city')
    input3.send_keys('Glasgow')
    input4 = browser.find_element(By.CSS_SELECTOR, "#country")
    input4.send_keys("Scotland")
    button = browser.find_element(By.TAG_NAME, 'button')
    button.click()


finally:
    time.sleep(30)
    browser.quit()