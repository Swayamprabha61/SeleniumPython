from selenium import webdriver
from selenium.webdriver.common.by import By

def test_webtable1():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/webtable1.html")
    table_body = driver.find_element(By.XPATH,"//table[@summary = 'Sample Table']/tbody")
    table_row = table_body.find_elements(By.TAG_NAME, 'tr')
    #or , driver.find_elements(By.XPATH,//table[@summary = 'Sample Tbale']/tbody/tr)

    for row in table_row:
        cols = row.find_elements(By.TAG_NAME, 'td')
        for e in cols:
            print(e.text)
            if 'Dubai' in e.text:
                print("YES")

