import pytest
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from pages.login_page import LoginPage

URL = "https://practicetestautomation.com/practice-test-login/"

def get_chrome_options(headless=True):
   options = Options()
   if headless:
       options.add_argument("--headless")
       options.add_argument("--disable-gpu")
       options.add_argument("--window-size=1920,1080")
   options.add_argument("--no-sandbox")
   options.add_argument("--disable-dev-shm-usage")
   options.add_argument("--disable-extensions")
   return options

@pytest.fixture
def driver():
   options = get_chrome_options(headless=True)
   driver  = webdriver.Chrome(
       service=Service(ChromeDriverManager().install()),
       options=options
   )
   driver.implicitly_wait(5)
   yield driver
   driver.quit()

def test_valid_login(driver):
   """Valid credentials should navigate to the success page"""
   page = LoginPage(driver)
   page.open(URL)
   page.login("student", "Password123")
   assert "Logged In" in page.get_success_heading()
   assert page.is_logout_visible()
   driver.save_screenshot("valid_login.png")
def test_invalid_password(driver):
   """Wrong password should display an error message"""
   page = LoginPage(driver)
   page.open(URL)
   page.login("student", "wrong password")
   assert "Your password is invalid" in page.get_error_message()
   driver.save_screenshot("invalid_password.png")
def test_invalid_username(driver):
   """Wrong username should display an error message"""
   page = LoginPage(driver)
   page.open(URL)
   page.login("wrong user", "Password123")
   assert "Your username is invalid" in page.get_error_message()
   driver.save_screenshot("invalid_username.png")
def test_empty_login(driver):
   """Empty submission should display a validation error"""
   page = LoginPage(driver)
   page.open(URL)
   page.click_submit()
   assert "Your username is invalid" in page.get_error_message()
   driver.save_screenshot("empty_login.png")
def test_page_title(driver):
   """Browser tab title should contain the word Practice"""
   page = LoginPage(driver)
   page.open(URL)
   assert "Practice" in driver.title