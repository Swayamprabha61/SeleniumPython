import time

import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.mouse_button import MouseButton
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


def test_mouse_actions():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/selenium/mouse_interaction.html")
    Clickable = driver.find_element(By.ID, "clickable")
    actions = ActionChains(driver)
#click and hold actions in input box
    actions \
        .click_and_hold(Clickable).key_down(Keys.SHIFT) \
        .send_keys("selenium") \
        .key_up(Keys.SHIFT).perform()
#click on the link
    click_on_link = driver.find_element(By.ID, "click")
    actions.click(click_on_link).perform()

    assert "resultPage" in driver.current_url

#with the help of action builder class you can back

    actions_builder = ActionBuilder(driver)
    actions_builder.pointer_action.pointer_down(MouseButton.BACK)
    actions_builder.pointer_action.pointer_down(MouseButton.BACK)
    actions_builder.perform()
    time.sleep(20)
   # actions_builder.pointer_action.pointer_up(MouseButton.LEFT).perform()

