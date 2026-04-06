from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime

BASE_URL  = "https://the-internet.herokuapp.com"
TIMEOUT   = 10

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(5)
wait   = WebDriverWait(driver, TIMEOUT)
passed = False
print(f"\n{'='*50}")
print("  DAY 4 - Tabs, Alerts & Dropdowns")
print(f"  {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print(f"{'='*50}")
try:

   print("\n── Part 1: Dropdown ──")
   driver.get(f"{BASE_URL}/dropdown")
   driver.maximize_window()
   print("[1] Dropdown page opened ")
   dropdown = Select(driver.find_element(By.ID, "dropdown"))
   dropdown.select_by_visible_text("Option 1")
   print(f"[2] Selected: '{dropdown.first_selected_option.text}' ")
   dropdown.select_by_value("2")
   print(f"[3] Selected: '{dropdown.first_selected_option.text}' ")
   dropdown.select_by_index(1)
   print(f"[4] Selected by index: '{dropdown.first_selected_option.text}' ")
   driver.save_screenshot("day4_dropdown.png")
   print("[5] Dropdown screenshot saved")


   print("\n── Part 2: Alerts ──")
   driver.get(f"{BASE_URL}/javascript_alerts")
   print("[6] Alerts page opened")
   driver.find_element(By.XPATH, "//button[text()='Click for JS Alert']").click()
   alert = wait.until(EC.alert_is_present())
   print(f"[7] Alert text: '{alert.text}' ")
   alert.accept()
   print("[8] Alert accepted")
   driver.find_element(By.XPATH, "//button[text()='Click for JS Confirm']").click()
   confirm = wait.until(EC.alert_is_present())
   print(f"[9] Confirm text: '{confirm.text}' ")
   confirm.dismiss()
   print("[10] Confirm dismissed")
   driver.find_element(By.XPATH, "//button[text()='Click for JS Prompt']").click()
   prompt = wait.until(EC.alert_is_present())
   prompt.send_keys("Hello Hari!")
   prompt.accept()
   print("[11] Prompt filled and accepted")
   driver.save_screenshot("day4_alerts.png")
   print("[12] Alerts screenshot saved")

   print("\n── Part 3: Multiple Tabs ──")
   driver.get(f"{BASE_URL}/windows")
   print("[13] Windows page opened ")
   original_tab = driver.current_window_handle
   print(f"[14] Original tab saved: {original_tab} ")
   driver.find_element(By.LINK_TEXT, "Click Here").click()
   wait.until(EC.number_of_windows_to_be(2))
   all_tabs = driver.window_handles
   print(f"[15] Total tabs open: {len(all_tabs)} ")
   new_tab = [tab for tab in all_tabs if tab != original_tab][0]
   driver.switch_to.window(new_tab)
   print(f"[16] Switched to new tab ")
   heading = wait.until(EC.visibility_of_element_located((By.TAG_NAME, "h3")))
   print(f"[17] New tab heading: '{heading.text}'")
   driver.save_screenshot("day4_new_tab.png")
   print("[18] New tab screenshot saved")
   driver.switch_to.window(original_tab)
   print(f"[19] Switched back to original tab")
   driver.save_screenshot("day4_original_tab.png")
   passed = True
except TimeoutException:
   print(f"\nTIMEOUT: Element did not appear within {TIMEOUT}s")
   driver.save_screenshot("day4_error.png")
except Exception as e:
   print(f"\n ERROR: {e}")
finally:
   driver.quit()
   print(f"\n{'='*50}")
   print(f"  RESULT: {'PASSED' if passed else 'FAILED'}")
   print(f"{'='*50}\n")