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
def test_js_execute(driver):
    url = "https://selectorshub.com/xpath-practice-page/"
    driver.get(url)

    # Locate the parent shadow host element
    div = driver.find_element(By.XPATH, "//div[@class='jackPart']")

    # Scroll the shadow host element into view using JavaScript
    driver.execute_script("arguments[0].scrollIntoView(true);", div)
    driver.execute_script("return document.querySelector('div#userName')\
                        .shadowRoot.querySelector('div#app2')\
                        .shadowRoot.querySelector('input#pizza');")
    # Execute JavaScript to find the shadow DOM element and interact with it

    # Send keys to the shadow DOM input element
    #ele.send_keys("Farmhouse")


    time.sleep(5)
