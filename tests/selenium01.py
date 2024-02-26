import pytest
from selenium import webdriver


@pytest.fixture()
def browser():
    driver = webdriver.Chrome()
    yield driver

def test_openbrowser(browser):
    browser.get("https://app.vwo.com")
    print(browser.title)
    assert "Login - VWO" == browser.title
