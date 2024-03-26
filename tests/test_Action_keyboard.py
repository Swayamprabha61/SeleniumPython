import time

import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains

def test_Action_keyboard():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/selenium/single_text_input.html")
    actions = ActionChains(driver)

    actions.send_keys("Selenium")   #autofocus on the input box is already there
    time.sleep(20)