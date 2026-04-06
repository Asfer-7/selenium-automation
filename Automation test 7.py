import pytest
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.login_page import LoginPage

URL     = "https://practicetestautomation.com/practice-test-login/"

@pytest.fixture
def driver():
   driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
   driver.implicitly_wait(5)
   driver.maximize_window()
   yield driver
   driver.quit()

def test_valid_login(driver):
   page = LoginPage(driver)
   page.open(URL)
   page.login("student", "Password123")
   assert "Logged In" in page.get_success_heading()
   assert page.is_logout_visible()
   driver.save_screenshot("valid_login.png")
def test_invalid_password(driver):
   page = LoginPage(driver)
   page.open(URL)
   page.login("student", "wrongpassword")
   assert "Your password is invalid" in page.get_error_message()
   driver.save_screenshot("invalid_password.png")
def test_invalid_username(driver):
   page = LoginPage(driver)
   page.open(URL)
   page.login("wrong user", "Password123")
   assert "Your username is invalid" in page.get_error_message()
   driver.save_screenshot("invalid_username.png")
def test_empty_login(driver):
   page = LoginPage(driver)
   page.open(URL)
   page.click_submit()
   assert "Your username is invalid" in page.get_error_message()
   driver.save_screenshot("empty_login.png")ŚḌ