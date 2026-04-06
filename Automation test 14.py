import pytest
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from login_page import LoginPage

URL = "https://practicetestautomation.com/practice-test-login/"

# Login Tests

def test_valid_login(driver):
   """Valid credentials should reach success page"""
   page = LoginPage(driver)
   page.open(URL)
   page.login("student", "Password123")
   assert "Logged In" in page.get_success_heading()
   assert page.is_logout_visible()
   driver.save_screenshot("parallel_valid_login.png")
def test_invalid_password(driver):
   """Wrong password should show error message"""
   page = LoginPage(driver)
   page.open(URL)
   page.login("student", "wrong password")
   assert "Your password is invalid" in page.get_error_message()
   driver.save_screenshot("parallel_invalid_password.png")
def test_invalid_username(driver):
   """Wrong username should show error message"""
   page = LoginPage(driver)
   page.open(URL)
   page.login("wrong "
              "user", "Password123")
   assert "Your username is invalid" in page.get_error_message()
   driver.save_screenshot("parallel_invalid_username.png")
def test_empty_login(driver):
   """Empty submission should show validation error"""
   page = LoginPage(driver)
   page.open(URL)
   page.click_submit()
   assert "Your username is invalid" in page.get_error_message()
   driver.save_screenshot("parallel_empty_login.png")

#Page Verification Tests

def test_page_title(driver):
   """Browser tab title should contain Practice"""
   page = LoginPage(driver)
   page.open(URL)
   assert "Practice" in driver.title
def test_page_url(driver):
   """Page URL should load correctly"""
   page = LoginPage(driver)
   page.open(URL)
   assert "practice-test-login" in driver.current_url
def test_success_url(driver):
   """URL should change after successful login"""
   page = LoginPage(driver)
   page.open(URL)
   page.login("student", "Password123")
   assert "logged-in-successfully" in driver.current_url
   driver.save_screenshot("parallel_success_url.png")
