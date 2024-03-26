import time

import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.common.by import By


def test_scroll():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://awesomeqa.com/selenium/frame_with_nested_scrolling_frame_out_of_view.html")

    iframe = driver.find_element(By.TAG_NAME, "iframe")
    scroll_origin = ScrollOrigin.from_element(iframe)

    action = ActionChains(driver)
    #if you want to scroll within the iframe then you need to use
    # scrollOrigin class ->scroll_from_origin(iframe_name, start position , scroll end position)
    action.scroll_from_origin(scroll_origin, 0, 200).perform()
    # action.scroll_to_element(iframe).perform()
    time.sleep(20)
