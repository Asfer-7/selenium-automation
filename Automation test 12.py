import pytest
import sys
import os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from login_page import LoginPage
URL = "https://practicetestautomation.com/practice-test-login/"

#Login Validation Tests

def test_valid_login_success(driver):
   """Full flow: open page → login → verify heading → verify logout button"""
   page = LoginPage(driver)
   page.open(URL)
   page.login("student", "Password123")
   assert "Logged In" in page.get_success_heading()
   assert page.is_logout_visible()
   driver.save_screenshot("e2e_valid_login.png")
def test_invalid_password_shows_error(driver):
   """Full flow: open page → wrong password → verify correct error"""
   page = LoginPage(driver)
   page.open(URL)
   page.login("student", "wrongpassword")
   assert "Your password is invalid" in page.get_error_message()
   driver.save_screenshot("e2e_invalid_password.png")
def test_invalid_username_shows_error(driver):
   """Full flow: open page → wrong username → verify correct error"""
   page = LoginPage(driver)
   page.open(URL)
   page.login("wronguser", "Password123")
   assert "Your username is invalid" in page.get_error_message()
   driver.save_screenshot("e2e_invalid_username.png")
def test_empty_submission_shows_error(driver):
   """Full flow: open page → submit empty → verify validation error"""
   page = LoginPage(driver)
   page.open(URL)
   page.click_submit()
   assert "Your username is invalid" in page.get_error_message()
   driver.save_screenshot("e2e_empty_submission.png")

#Page Verification Tests

def test_page_title_is_correct(driver):
   """Verify browser tab title contains expected text"""
   page = LoginPage(driver)
   page.open(URL)
   assert "Practice" in driver.title
def test_page_url_is_correct(driver):
   """Verify the page URL loads correctly"""
   page = LoginPage(driver)
   page.open(URL)
   assert "practice-test-login" in driver.current_url
def test_success_url_after_login(driver):
   """Verify URL changes correctly after successful login"""
   page = LoginPage(driver)
   page.open(URL)
   page.login("student", "Password123")
   assert "logged-in-successfully" in driver.current_url
   driver.save_screenshot("e2e_url_verified.png")

#Data Driven Tests from Excel

from excel_reader import read_excel_data
EXCEL_FILE = os.path.join(os.path.dirname(__file__), "login_data.xlsx")
test_data  = read_excel_data(EXCEL_FILE)
@pytest.mark.parametrize("username, password, expected", test_data)
def test_login_data_driven(driver, username, password, expected):
   """Data driven login test — one run per Excel row"""
   page = LoginPage(driver)
   page.open(URL)
   page.login(username, password)
   screenshot_name = f"e2e_excel_{username or 'empty'}.png"
   driver.save_screenshot(screenshot_name)
   if "Logged In" in expected:
       assert expected in page.get_success_heading()
   else:
       assert expected in page.get_error_message()