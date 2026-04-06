from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class LoginPage:

   USERNAME_INPUT = (By.ID, "username")
   PASSWORD_INPUT = (By.NAME, "password")
   SUBMIT_BUTTON  = (By.ID, "submit")
   ERROR_MESSAGE  = (By.ID, "error")
   SUCCESS_HEADING = (By.CSS_SELECTOR, "h1.post-title")
   LOGOUT_BUTTON  = (By.LINK_TEXT, "Log out")
   def __init__(self, driver):
       self.driver = driver
       self.wait   = WebDriverWait(driver, 10)

   def open(self, url):
       self.driver.get(url)
   def enter_username(self, username):
       field = self.wait.until(EC.element_to_be_clickable(self.USERNAME_INPUT))
       field.clear()
       field.send_keys(username)
   def enter_password(self, password):
       field = self.wait.until(EC.element_to_be_clickable(self.PASSWORD_INPUT))
       field.clear()
       field.send_keys(password)
   def click_submit(self):
       self.wait.until(EC.element_to_be_clickable(self.SUBMIT_BUTTON)).click()
   def login(self, username, password):
       self.enter_username(username)
       self.enter_password(password)
       self.click_submit()
   def get_success_heading(self):
       return self.wait.until(
           EC.visibility_of_element_located(self.SUCCESS_HEADING)
       ).text
   def get_error_message(self):
       return self.wait.until(
           EC.visibility_of_element_located(self.ERROR_MESSAGE)
       ).text
   def is_logout_visible(self):
       try:
           self.wait.until(EC.visibility_of_element_located(self.LOGOUT_BUTTON))
           return True
       except:
           return False