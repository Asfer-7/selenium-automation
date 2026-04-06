import pytest
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.login_page import LoginPage
from datetime import datetime

URL = "https://practicetestautomation.com/practice-test-login/"

@pytest.fixture
def driver():
   driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
   driver.implicitly_wait(5)
   driver.maximize_window()
   yield driver
   driver.quit()

def pytest_html_report_title(report):
   report.title = "Report"

def test_valid_login(driver):
   """Valid credentials should land on the success page"""
   page = LoginPage(driver)
   page.open(URL)
   page.login("student", "Password123")
   assert "Logged In" in page.get_success_heading()
   assert page.is_logout_visible()
   driver.save_screenshot("valid_login.png")
def test_invalid_password(driver):
   """Wrong password should show an error message"""
   page = LoginPage(driver)
   page.open(URL)
   page.login("student", "wrongpassword")
   assert "Your password is invalid" in page.get_error_message()
   driver.save_screenshot("invalid_password.png")
def test_invalid_username(driver):
   """Wrong username should show an error message"""
   page = LoginPage(driver)
   page.open(URL)
   page.login("wronguser", "Password123")
   assert "Your username is invalid" in page.get_error_message()
   driver.save_screenshot("invalid_username.png")
def test_empty_login(driver):
   """Empty fields should show a validation error"""
   page = LoginPage(driver)
   page.open(URL)
   page.click_submit()
   assert "Your username is invalid" in page.get_error_message()
   driver.save_screenshot("empty_login.png")
def test_page_title(driver):
   """Browser tab title should contain Practice"""
   page = LoginPage(driver)
   page.open(URL)
   assert "Practice" in driver.title