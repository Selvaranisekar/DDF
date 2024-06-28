from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage():

    def __init__(self,browser):
        self.browser=browser

    def login(self,username,password):
        username_input=WebDriverWait(self.browser,10).until(EC.presence_of_element_located((By.ID,"username")))
        username_input.send_keys(username)
        password_input=WebDriverWait(self.browser,10).until(EC.presence_of_element_located((By.ID,"password")))
        password_input.send_keys(password)

        login_button=WebDriverWait(self.browser,10).until(EC.presence_of_element_located((By.ID,"login_button")))
        login_button.click()

