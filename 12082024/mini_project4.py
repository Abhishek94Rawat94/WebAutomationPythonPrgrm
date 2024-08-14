#- Mini Project 4
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import allure


@pytest.mark.positive
@allure.title("Verify that URL changes")
@allure.description("Verify the current and next page URL changes by making appointment")
def test_mini_project4():
    driver = webdriver.Chrome()
    #open the url
    driver.get("https://katalon-demo-cura.herokuapp.com/")

    # Click on url
    make_appointment_element = driver.find_element(By.ID, "btn-make-appointment")
    make_appointment_element.click()

    # Verify the changed URl
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/profile.php#login"
    time.sleep(3)
    # Enter username and password
    username = driver.find_element(By.ID, "txt-username")
    username.send_keys("John Doe")

    password = driver.find_element(By.ID,"txt-password")
    password.send_keys("ThisIsNotAPassword")

    # Clicking on Login button
    login_button = driver.find_element(By.ID,"btn-login")
    login_button.click()
    time.sleep(3)

    # Next page verify the current url
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/#appointment"
    time.sleep(5)

    # Verify the Make Appointment
    make_appointment = driver.find_element(By.TAG_NAME, "h2")
    assert make_appointment.text == "Make Appointment"

    # For allure screenshot
    allure.attach(driver.get_screenshot_as_png(),name='appointment_screenshot')

    driver.quit()


