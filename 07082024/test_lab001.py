from selenium import webdriver
import time


def test_sample():
    driver = webdriver.Edge()
    driver.get("https://www.google.com")
    time.sleep(5)
    
