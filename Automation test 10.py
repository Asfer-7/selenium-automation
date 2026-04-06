import pytest
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from pages.login_page import LoginPage
from utilities.excel_reader import read_excel_data

URL = "https://practicetestautomation.com/practice-test-login/"
EXCEL_FILE = os.path.join(os.path.dirname(__file__), "login_data.xlsx")
test_data = read_excel_data(EXCEL_FILE)
def get_chrome_options(headless=True):
    options = Options()
    if headless:
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        options.add_argument("--window-size=1920,1080")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    return options
@pytest.fixture
def driver():
    options = get_chrome_options(headless=True)
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )
    driver.implicitly_wait(5)
    yield driver
    driver.quit()
@pytest.mark.parametrize("username, password, expected", test_data)
def test_login_with_excel_data(driver, username, password, expected):
    """Login test driven by Excel data — runs once per row"""
    page = LoginPage(driver)
    page.open(URL)
    page.login(username, password)
    screenshot_name = f"login_{username or 'empty'}.png"
    driver.save_screenshot(screenshot_name)
    if "Logged In" in expected:
        assert expected in page.get_success_heading()
    else:
        assert expected in page.get_error_message()