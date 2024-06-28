import os

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def verify_ifloginsuccess(browser):
    try:
        assert "inventory" in browser.current_url.lower(),"Login has Failed"
    except AssertionError as e:
        save_screenshot(browser)
        raise AssertionError("Login has failed") from e

def login(browser):
    save_screenshot(browser)

# def login_test(browser,username,password):
    # username_input = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, "username")))
    # username_input.send_keys(username)
    # password_input = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, "password")))
    # password_input.send_keys(password)
    #
    # login_button = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, "login_button")))
    # login_button.click()

def save_screenshot(browser):
    screenshot_dir=os.path.join(os.getcwd(),'screenshot')
    os.makeddirs(screenshot_dir,exist_ok=True)
    screenshot_path=os.path.join(screenshot_dir,f"login_failure.png")
    browser.save_screenshot(screenshot_path)
    print(f"screenshot saved at:{screenshot_path}")

