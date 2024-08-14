# 1 Open the URL - https://www.idrive360.com/enterprise/login
# 2 Enter the username, password
# 3 Verify that Trial is fnished and current URL also
# 4 Add a logic to add Allure Screen for the Trail end


from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import allure
import time


@pytest.mark.positive
@allure.title("Verify that Trial is fnished and current URL also")
@allure.description("Verify the idrive360 URL and trial")
def test_mini_project3():
    # Navigate to URL
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.idrive360.com/enterprise/login")

    # Enter username and password
    email_element = driver.find_element(By.ID, "username")
    email_element.send_keys("augtest_040823@idrive.com")
    time.sleep(5)

    password_element = driver.find_element(By.ID, "password")
    password_element.send_keys("123456")
    time.sleep(5)

    signin_button_element = driver.find_element(By.ID, "frm-btn")
    signin_button_element.click()
    time.sleep(25)

    # Verify the trial is finished and also the URL
    assert driver.current_url == "https://www.idrive360.com/enterprise/account?upgradenow=true"

    message_alert = driver.find_element(By.CLASS_NAME,"id-card-title")
    assert message_alert.is_displayed()
    time.sleep(5)
    allure.attach(driver.get_screenshot_as_png(), name='upgrade_Screenshot')
    driver.quit()

