import time

import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.common.by import By

def test_makemytrip():
    driver = webdriver.Chrome()
    driver.get("https://www.makemytrip.com/")
    time.sleep(5)
    from_city = driver.find_element(By.ID, "fromCity")
    actions = ActionChains(driver)
    actions.move_to_element(from_city).click().send_keys("New Delhi").perform()