import pytest
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pages.login_page import LoginPage
URL = "https://practicetestautomation.com/practice-test-login/"
def test_valid_login(driver):
   """Valid login should reach the success page"""
   page = LoginPage(driver)
   page.open(URL)
   page.login("student", "Password123")
   assert "Logged In" in page.get_success_heading()
   assert page.is_logout_visible()
def test_invalid_password(driver):
   """Wrong password should show error message"""
   page = LoginPage(driver)
   page.open(URL)
   page.login("student", "wrong password")
   assert "Your password is invalid" in page.get_error_message()
def test_invalid_username(driver):
   """Wrong username should show error message"""
   page = LoginPage(driver)
   page.open(URL)
   page.login("wrong user", "Password123")
   assert "Your username is invalid" in page.get_error_message()
def test_empty_login(driver):
   """Empty submission should show validation error"""
   page = LoginPage(driver)
   page.open(URL)
   page.click_submit()
   assert "Your username is invalid" in page.get_error_message()
def test_intentional_fail(driver):
   """This test is intentionally wrong to trigger auto screenshot"""
   page = LoginPage(driver)
   page.open(URL)
   page.login("student", "Password123")
   assert "WRONG TEXT" in page.get_success_heading()