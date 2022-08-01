from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc_fun(data):
    return str(math.log(abs(12*math.sin(int(data)))))

try:
    link = "https://suninjuly.github.io/math.html"
    with webdriver.Chrome() as browser:
        browser.get(link)
        people_radio = browser.find_element(By.ID, 'peopleRule')
        people_checked = people_radio.get_attribute("checked")
        print("value of people radio: ", people_checked)

        assert people_checked == 'true', 'Radiobutton is not selected by default'

        robots_radio = browser.find_element(By.ID, "robotsRule")
        robots_checked = robots_radio.get_attribute("checked")
        assert robots_checked is None, 'Radiobutton is not selected by default'


finally:
    print("Test has been complited")