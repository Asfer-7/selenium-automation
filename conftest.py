import pytest
import os
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

SCREENSHOT_DIR = "failure_screenshots"
os.makedirs(SCREENSHOT_DIR, exist_ok=True)

def pytest_addoption(parser):
   parser.addoption(
       "--browser",
       action="store",
       default="chrome",
       help="Browser to run tests on: chrome, firefox, edge"
   )
@pytest.fixture
def driver(request):
   browser = request.config.getoption("--browser").lower()
   if browser == "chrome":
       options = ChromeOptions()
       options.add_argument("--headless")
       options.add_argument("--disable-gpu")
       options.add_argument("--window-size=1920,1080")
       options.add_argument("--no-sandbox")
       options.add_argument("--disable-dev-shm-usage")
       driver = webdriver.Chrome(
           service=ChromeService(ChromeDriverManager().install()),
           options=options

       )
   elif browser == "edge":
       options = EdgeOptions()
       options.add_argument("--no-sandbox")
       options.add_argument("--disable-dev-shm-usage")
       options.add_argument("--disable-web-security")
       options.add_argument("--allow-running-insecure-content")
       options.add_argument("--window-size=1920,1080")
       options.use_chromium = True
       driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()),
       options=options
   )
   else:
       raise ValueError(f"Browser '{browser}' not supported. Use chrome, firefox or edge")
   driver.implicitly_wait(5)
   yield driver
   driver.quit()
# ── AUTO SCREENSHOT ON FAILURE ────────────────────────────────
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
   outcome = yield
   report  = outcome.get_result()
   if report.when == "call" and report.failed:
       driver = item.funcargs.get("driver")
       if driver:
           timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
           test_name = item.name.replace(" ", "_")
           filename  = f"{SCREENSHOT_DIR}/{test_name}_{timestamp}.png"
           driver.save_screenshot(filename)
           print(f"\n📸 Failure screenshot: {filename}")