import pytest
import logging

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

@pytest.mark.negative
def test_katalon_appointment_negative():
    #LOGGER = logging.getLogger(__name__)
    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    driver.maximize_window()

    driver.find_element(By.LINK_TEXT, "Make Appointment").click()
    driver.find_element(By.ID, "txt-username").send_keys("swayam12")
    driver.find_element(By.NAME, "password").send_keys("This@123")
    driver.find_element(By.ID, "btn-login").click()

    error_message = driver.find_element(By.CSS_SELECTOR, "p.lead.text-danger")
    assert "Login failed!" in error_message.text

@pytest.mark.positive
def test_katalon_appointment_positive():
    #LOGGER = logging.getLogger(__name__)
    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    driver.maximize_window()

    # Test case to automate - manual Testing
    # Open - https://katalon-demo-cura.herokuapp.com/
    # Click on the make Appointment
    # Put username , password and click Login
    # Select the 2 option from drop down, Radio, 2 checkbox
    # enter the date and Text and click Book Appointment
    # verify that the Appointment Confirmation message is visible on the page.

    driver.find_element(By.LINK_TEXT, "Make Appointment").click()
    driver.find_element(By.ID, "txt-username").send_keys("John Doe")
    driver.find_element(By.NAME, "password").send_keys("ThisIsNotAPassword")
    driver.find_element(By.ID, "btn-login").click()

    #select options from dropdown
    dropdown = Select(driver.find_element(By.ID,"combo_facility"))
    dropdown.select_by_visible_text("Hongkong CURA Healthcare Center")

    #click on the checkbox
    driver.find_element(By.ID, "chk_hospotal_readmission").click()

    #find the programs (radio button)
    driver.find_element(By.NAME, "programs").click()

    # pass the date of booking
    driver.find_element(By.ID, "txt_visit_date").send_keys("12/03/2024")
    #give the reason in the comment box
    driver.find_element(By.NAME, "comment").send_keys("I have cold with fever")
    # click on the book appointment button
    driver.find_element(By.ID,"btn-book-appointment").click()

    heading_h2 = driver.find_element(By.TAG_NAME, "h2")
    assert "Appointment Confirmation" in heading_h2.text