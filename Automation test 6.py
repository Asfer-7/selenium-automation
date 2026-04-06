import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

URL      = "https://practicetestautomation.com/practice-test-login/"
TIMEOUT  = 15

@pytest.fixture
def driver():
   driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
   driver.implicitly_wait(10)
   driver.maximize_window()
   yield driver
   driver.quit()

def test_valid_login(driver):
   wait = WebDriverWait(driver, TIMEOUT)
   driver.get(URL)
   driver.find_element(By.ID, "username").send_keys("student")
   driver.find_element(By.NAME, "password").send_keys("Password123")
   driver.find_element(By.ID, "submit").click()
   heading = wait.until(
       EC.visibility_of_element_located((By.CSS_SELECTOR, "h1.post-title"))
   )
   driver.save_screenshot("valid_login.png")
   assert "Logged In" in heading.text

def test_invalid_login(driver):
   wait = WebDriverWait(driver, TIMEOUT)
   driver.get(URL)
   driver.find_element(By.ID, "username").send_keys("student")
   driver.find_element(By.NAME, "password").send_keys("wrong password")
   driver.find_element(By.ID, "submit").click()
   error = wait.until(
       EC.visibility_of_element_located((By.ID, "error"))
   )
   driver.save_screenshot("invalid_login.png")
   assert "Your password is invalid" in error.text

def test_empty_fields(driver):
   wait = WebDriverWait(driver, TIMEOUT)
   driver.get(URL)
   driver.find_element(By.ID, "submit").click()
   error = wait.until(
       EC.visibility_of_element_located((By.ID, "error"))
   )
   driver.save_screenshot("empty_fields.png")
   assert "Your username is invalid" in error.text

def test_page_title(driver):
   driver.get(URL)
   assert "Practice" in driver.title
