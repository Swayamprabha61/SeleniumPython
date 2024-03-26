import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from tests.utils.JSUtil import JSUtils


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.mark.usefixtures("driver")
def test_js_executor(driver):
    URL = "https://the-internet.herokuapp.com/add_remove_elements/"
    driver.get(URL)

    # create the object of JSUtils class --> utils where we have all the methods we can reuse in our code
    js_utils = JSUtils(driver)

    # through javascript object you can create alert

    # js_utils.make_alert("Hello")
    # time.sleep(6)

    # through js object you can click on element
    element = driver.find_element(By.XPATH, "//button[@onclick='addElement()']")
    js_utils.click_element_by_js(element)
    time.sleep(5)
    #refreshing the web page
    js_utils.refresh_browser_by_js(driver)
    #
