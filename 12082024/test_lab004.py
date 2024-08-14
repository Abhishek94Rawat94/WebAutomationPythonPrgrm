from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import allure


@pytest.mark.positive
@allure.title("Verify that URL changes when we click on make appointment button")
@allure.description("Verify the URL changes")
def test_mini_project1():
    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    # find the element the anchor tah
    # click on it
    make_appointment_element = driver.find_element(By.ID, "btn-make-appointment")

    # Click on it
    make_appointment_element.click()

    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/profile.php#login"
