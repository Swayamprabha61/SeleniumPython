import time

import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


def test_actions():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/practice.html")
    first_name = driver.find_element(By.NAME, "firstname")

    # create an object of ActionChain class
    actions = ActionChains(driver)
    # send keys but with the shift(for capital letter keys) #key_down -> press the key
    actions \
        .key_down(Keys.SHIFT).send_keys_to_element(first_name, "The Testing") \
        .key_up(Keys.SHIFT) \
        .perform()

    time.sleep(10)
    # Do right click on the link
    url = driver.find_element(By.PARTIAL_LINK_TEXT, "Click here to")
    actions.context_click(url).perform()  # or context_click(on_element=url).perform()
    # actions.send_keys("")
    time.sleep(10)

    #
