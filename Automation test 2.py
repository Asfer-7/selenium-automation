from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime

URL      = "https://practicetestautomation.com/practice-test-login/"
USERNAME = "student"
PASSWORD = "Password123"
TIMEOUT  = 10

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
wait   = WebDriverWait(driver, TIMEOUT)
passed = False
print(f"\n{'='*50}")
print("  DAY 2 - Login Automation Test")
print(f"  {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print(f"{'='*50}")
try:

   driver.get(URL)
   driver.maximize_window()
   print("\n[1] Page opened ")
   driver.find_element(By.ID, "username").send_keys(USERNAME)
   print("[2] Username entered ")
   driver.find_element(By.NAME, "password").send_keys(PASSWORD)
   print("[3] Password entered ")
   driver.find_element(By.XPATH, "//button[@id='submit']").click()
   print("[4] Login button clicked ")
   success_msg = wait.until(
       EC.visibility_of_element_located((By.CSS_SELECTOR, "h1.post-title"))
   )
   print(f"[5] Page heading: '{success_msg.text}' ")
   assert "Logged In" in success_msg.text, "Login verification failed!"
   driver.save_screenshot("Automation login.png")
   print("[6] Screenshot saved ")
   passed = True
   print("\n── Negative Test (Wrong Password) ──")
   driver.get(URL)
   driver.find_element(By.ID, "username").send_keys("student")
   driver.find_element(By.NAME, "password").send_keys("wrong password")
   driver.find_element(By.XPATH, "//button[@id='submit']").click()
   error_msg = wait.until(
       EC.visibility_of_element_located((By.ID, "error"))
   )
   print(f"[BONUS] Error message shown: '{error_msg.text}' ")
   driver.save_screenshot("Login fail.png")
except AssertionError as e:
   print(f"\n ASSERTION FAILED: {e}")
except Exception as e:
   print(f"\n ERROR: {e}")
finally:
   driver.quit()
   print(f"\n{'='*50}")
   print(f"  RESULT: {'PASSED' if passed else ' FAILED'}")
   print(f"{'='*50}\n")