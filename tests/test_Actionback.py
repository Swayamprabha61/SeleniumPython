import time
import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

def test_mouse_actions():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/selenium/mouse_interaction.html")

    # Click and hold actions in input box
    clickable = driver.find_element(By.ID, "clickable")
    actions = ActionChains(driver)
    actions.click_and_hold(clickable).key_down(Keys.SHIFT) \
        .send_keys("selenium").key_up(Keys.SHIFT).perform()

    # Click on the link
    click_on_link = driver.find_element(By.ID, "click")
    actions = ActionChains(driver)
    actions.click(click_on_link).perform()

    assert "resultPage" in driver.current_url

    # Using the back button
    actions = ActionChains(driver)
    actions.send_keys(Keys.BACK_SPACE).perform()  # This is the correct way to simulate "Back" action

    time.sleep(5)  # Add a sleep to observe the result

    #driver.quit()

# Run the test function

