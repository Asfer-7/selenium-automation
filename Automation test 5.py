from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime
import os

BASE_URL = "https://the-internet.herokuapp.com"
TIMEOUT  = 15

driver  = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
wait    = WebDriverWait(driver, TIMEOUT)
actions = ActionChains(driver)
passed  = False
print(f"\n{'='*50}")
print("File Uploads, Scrolling & Mouse Actions")
print(f"  {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print(f"{'='*50}")
try:

   print("\n── Part 1: File Upload ──")
   test_file = os.path.abspath("test_upload.txt")
   with open(test_file, "w") as f:
       f.write("This is a file for automation test")
   print("[1] Test file created ")
   driver.get(f"{BASE_URL}/upload")
   driver.maximize_window()
   print("[2] Upload page opened")
   upload_input = driver.find_element(By.ID, "file-upload")
   upload_input.send_keys(test_file)
   print("[3] File path sent to upload input ")
   driver.find_element(By.ID, "file-submit").click()
   print("[4] Upload button clicked")
   confirmation = wait.until(
       EC.visibility_of_element_located((By.ID, "uploaded-files"))
   )
   print(f"[5] Upload confirmed: '{confirmation.text}'")
   driver.save_screenshot("file_upload.png")
   print("[6] Screenshot saved")

   print("\n── Scrolling ──")
   driver.get(f"{BASE_URL}/large")
   print("[7] Large page opened ")
   driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
   print("[8] Scrolled to bottom")
   driver.save_screenshot("scroll_bottom.png")
   driver.execute_script("window.scrollTo(0, 0);")
   print("[9] Scrolled back to top ")
   target_element = driver.find_element(By.LINK_TEXT, "Large & Deep DOM")
   driver.execute_script("arguments[0].scrollIntoView();", target_element)
   print("[10] Scrolled to specific element ")
   driver.save_screenshot("scroll_element.png")

   print("\n── Mouse Actions ──")
   driver.get(f"{BASE_URL}/hovers")
   print("[11] Hovers page opened ")
   avatar = wait.until(
       EC.presence_of_element_located((By.CLASS_NAME, "figure"))
   )
   actions.move_to_element(avatar).perform()
   print("[12] Hovered over element ")
   hidden_text = wait.until(
       EC.visibility_of_element_located((By.CSS_SELECTOR, ".figcaption h5"))
   )
   print(f"[13] Hidden text visible after hover: '{hidden_text.text}' ")
   driver.save_screenshot("hover.png")
   driver.get(f"{BASE_URL}/double_click")
   print("[14] Double click page opened ")
   box = wait.until(
       EC.presence_of_element_located((By.ID, "double-click"))
   )
   actions.double_click(box).perform()
   print("[15] Double clicked element ")
   driver.save_screenshot("double_click.png")
   driver.get(f"{BASE_URL}/context_menu")
   print("[16] Right click page opened")
   context_box = wait.until(
       EC.presence_of_element_located((By.ID, "hot-spot"))
   )
   actions.context_click(context_box).perform()
   print("[17] Right clicked element")
   alert = wait.until(EC.alert_is_present())
   print(f"[18] Alert text: '{alert.text}' ")
   alert.accept()
   driver.save_screenshot("right_click.png")
   passed = True
except TimeoutException:
   print(f"\n TIMEOUT: Element did not load within {TIMEOUT}s")
   driver.save_screenshot("Error.png")
except Exception as e:
   print(f"\n ERROR: {e}")
finally:
   driver.quit()
   print(f"\n{'='*50}")
   print(f"  RESULT: {' PASSED' if passed else ' FAILED'}")
   print(f"{'='*50}\n")