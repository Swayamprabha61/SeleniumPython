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
    url = "https://www.amcharts.com/svg-maps/?map=india"
    driver.get(url)
    driver.maximize_window()
    time.sleep(5)
    actions = ActionChains(driver)
    path_states = driver.find_elements(By.XPATH,
                                       "//*[local-name() = 'svg']/*[local-name()='g'][7]/*[local-name()='g']/*[local-name()='g']/*[local-name()= 'path']")
    for state in path_states:
        state_name = state.get_attribute("aria-label")
        print(state_name)
        if state_name == "Assam  ":
            actions.move_to_element(state).click().perform()
            time.sleep(10)
            break
    time.sleep(2)
