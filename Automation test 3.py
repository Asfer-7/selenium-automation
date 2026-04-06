from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime

URL      = "https://practicetestautomation.com/practice-test-login/"
USERNAME = "student"
PASSWORD = "Password123"
TIMEOUT  = 10

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(5)
wait   = WebDriverWait(driver, TIMEOUT)
passed = False
print(f"\n{'='*50}")
print(f"  {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print(f"{'='*50}")
try:
   driver.get(URL)
   driver.maximize_window()
   print("\n[1] Page opened ")
   username_field = wait.until(
       EC.element_to_be_clickable((By.ID, "username"))
   )
   username_field.send_keys(USERNAME)
   print("[2] Username entered ")
   password_field = wait.until(
       EC.visibility_of_element_located((By.NAME, "password"))
   )
   password_field.send_keys(PASSWORD)
   print("[3] Password entered ")
   submit_btn = wait.until(
       EC.element_to_be_clickable((By.ID, "submit"))
   )
   submit_btn.click()
   print("[4] Submit button clicked ")
   wait.until(EC.url_contains("logged-in-successfully"))
   print(f"[5] URL changed to: {driver.current_url} ")
   heading = wait.until(
       EC.visibility_of_element_located((By.CSS_SELECTOR, "h1.post-title"))
   )
   print(f"[6] Heading found: '{heading.text}' ")
   logout_btn = wait.until(
       EC.presence_of_element_located((By.LINK_TEXT, "Log out"))
   )
   print(f"[7] Logout button found: '{logout_btn.text}' ")
   assert "Logged In" in heading.text
   driver.save_screenshot("wait success.png")
   print("[8] Screenshot saved ")
   passed = True
   print("\n── Bonus: Testing Timeout Handling ──")
   try:
       WebDriverWait(driver, 3).until(
           EC.presence_of_element_located((By.ID, "non_existent_element"))
       )
   except TimeoutException:
       print("[BONUS] TimeoutException caught correctly ")
       print("        Element didn't appear — test handled it gracefully")
       driver.save_screenshot("timeout handled.png")
except TimeoutException as e:
   print(f"\n TIMEOUT: Element did not appear within {TIMEOUT}s")
   driver.save_screenshot("day3_error.png")
except AssertionError:
   print("\n ASSERTION FAILED: Page content did not match expected")
except Exception as e:
   print(f"\n UNEXPECTED ERROR: {e}")
finally:
   driver.quit()
   print(f"\n{'='*50}")
   print(f"  RESULT: {' PASSED' if passed else ' FAILED'}")
   print(f"{'='*50}\n")