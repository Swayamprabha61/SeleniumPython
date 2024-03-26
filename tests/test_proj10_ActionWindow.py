#OPen HEATMAP of vwo.com and click on iframe -> click map
#steps:
#1.open the link through webdriver
#2. Use Action to move the mouse to view Heatmap an dclick on it.
#3. Switch the window and Switch to iframe
#4.Click on button-> Click Map in the iframe of heatmap

from selenium import webdriver
import time
from selenium.webdriver.common.by import By


def test_window_handel():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com//windows")

    #found the currentwindow
    main_window = driver.current_window_handle
    print(main_window)
    #click the link on current window
    link = driver.find_element(By.LINK_TEXT, "Click Here")
    link.click()
    time.sleep(4)
    #check how many window are opened
    window_handle = driver.window_handles
    print(window_handle)

    #check that new window correct or not
    for handle in window_handle:
        if "New Window" in driver.page_source:
            print("page has found")
            break;

    #once verification done back to the main window
    driver.switch_to.window(main_window)
    time.sleep(2)