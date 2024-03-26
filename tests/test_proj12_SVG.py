import time

import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from tests.utils.JSUtil import JSUtils


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.mark.usefixtures("driver")
def test_js_executor(driver):
    url = "https://www.flipkart.com/"
    driver.get(url)
    time.sleep(5)
    driver.maximize_window()
    #button_cross = driver.find_element(By.XPATH,"//button[contains(text(),'x')]")
    actions = ActionChains(driver)
    #actions.move_to_element(button_cross).click().perform()
    search_input = driver.find_element(By.NAME, "q")
    search_input.send_keys("TV")
    #below code also works
    search_svg_icon = driver.find_element(By.XPATH, "//*[local-name()='svg' and @fill='none']")
    #search_icon = driver.find_element(By.XPATH,"//*[local-name()='svg']/*[local-name()='g' and@fill-rule = 'evenodd']")
    actions.move_to_element(search_svg_icon).click().perform()
    time.sleep(5)
    no_of_items = driver.find_element(By.XPATH,"//span[contains(text(),'results')]")
    print(no_of_items.text)


