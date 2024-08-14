from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import allure
import time


@pytest.mark.negative
def test_mini_project2():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://app.vwo.com/")

    #assert driver.current_url == "https://app.vwo.com/"
    # find the element the anchor tah
    # click on it
    # find the element username and enter the username
    username_element = driver.find_element(By.ID, "login-username")
    username_element.send_keys("adminadmin")

    # find the element password and enter the password
    # Click on it
    password_element = driver.find_element(By.ID, "login-password")
    password_element.send_keys("abcabc")

    # find sign-in button element and Click on signin button

    signin_element = driver.find_element(By.ID, "js-login-btn")
    signin_element.click()
    time.sleep(5)

    # Verify the invalid email password text messagemessage
    error_message = driver.find_element(By.ID,"js-notification-box-msg")

    assert error_message.text == "Your email, password, IP address or location did not match"
    time.sleep(10)
    driver.quit()