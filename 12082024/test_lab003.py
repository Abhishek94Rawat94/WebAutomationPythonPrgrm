from selenium import webdriver
import time

def test_open_wvologin():
    driver=webdriver.Chrome()
    driver.get("https://app.vwo.com")
    driver.refresh()
    driver.back()
    driver.forward()
    print(driver.page_source)
    print(driver.session_id)
    print(driver.title)
    assert driver.title == "Login - VWO"
    time.sleep(5)
    driver.quit()
