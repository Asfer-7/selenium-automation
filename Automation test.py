from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

try:
    print("Step 1: Navigating to Wikipedia...")
    driver.get("https://www.wikipedia.org/")
    driver.maximize_window()

    search_box = driver.find_element(By.ID, "searchInput")
    search_box.send_keys("React (software)")
    search_box.send_keys(Keys.RETURN)

    time.sleep(10)

    page_title = driver.find_element(By.ID, "firstHeading").text

    if "React" in page_title:
        print(f"SUCCESS: Found page heading: '{page_title}'")
        driver.save_screenshot("automation_evidence.png")
        print("Screenshot saved as 'automation_evidence.png'")
    else:
        print("FAILURE: Page heading did not match.")

finally:
    driver.quit()
    print("Test Completed and Browser Closed.")