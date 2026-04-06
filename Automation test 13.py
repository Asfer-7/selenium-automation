import pytest
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from login_page import LoginPage

URL = "https://practicetestautomation.com/practice-test-login/"

def test_valid_login(driver):
   """Valid login should reach success page on any browser"""
   page = LoginPage(driver)
   page.open(URL)
   page.login("student", "Password123")
   assert "Logged In" in page.get_success_heading()
   assert page.is_logout_visible()
   driver.save_screenshot(f"cross_browser_valid_login.png")

def test_invalid_password(driver):
   """Wrong password should show error on any browser"""
   page = LoginPage(driver)
   page.open(URL)
   page.login("student", "wrongpassword")
   assert "Your password is invalid" in page.get_error_message()
   driver.save_screenshot(f"cross_browser_invalid_password.png")

def test_invalid_username(driver):
   """Wrong username should show error on any browser"""
   page = LoginPage(driver)
   page.open(URL)
   page.login("wronguser", "Password123")
   assert "Your username is invalid" in page.get_error_message()
   driver.save_screenshot(f"cross_browser_invalid_username.png")

def test_page_title(driver):
   """Page title should be correct on any browser"""
   page = LoginPage(driver)
   page.open(URL)
   assert "Practice" in driver.title