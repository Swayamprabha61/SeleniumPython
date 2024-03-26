import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_webtables():
    driver = webdriver.Firefox()
    driver.get("https://awesomeqa.com/webtable.html")
    driver.maximize_window()

    row_element = driver.find_elements(By.XPATH, "//table[@id = 'customers']/tbody/tr")
    col_element = driver.find_elements(By.XPATH, "//table[@id = 'customers']/tbody/tr[2]/td")
    row = len(row_element)
    col = len(col_element)
    print(row)
    print(col)

    # getting the coloumns value
    # //table[@id = 'customers']/tbody/tr[1]/td[2]
    # or //table[contains(@id,'cust')]/tbody/tr[]/td[]

    first_data = "//table[@id='customers']/tbody/tr["
    second_data = "]/td["
    third_data = "]"

    for i in range(2, row + 1):
        for j in range(1, col + 1):
            dynamic_path = f"{first_data}{i}{second_data}{j}{third_data}"
            data = driver.find_element(By.XPATH, dynamic_path).text
            print(dynamic_path)
            print(data)

            # ques: find the country of "Helen Bennett"
            if "Helen Bennett" in data:
                country_path = f"{dynamic_path}/following-sibling::td"
                country_text = driver.find_element(By.XPATH, country_path).text
                print(f"Helen Bennett is in {country_text}")

            # similarly you can find the company of "Helen Bennet"

            if "Helen Bennett" in data:
                company_path = f"{dynamic_path}/preceding-sibling::td"
                company_name = driver.find_element(By.XPATH, company_path).text
                print(f"Helen Bennett company is {company_name}")
