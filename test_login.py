import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from dframework.Utilities.credential_reader import read_credentials_from_csv
from dframework.Utilities.selenium_util import verify_ifloginsuccess
@pytest.fixture(scope="session")
def browser():
    driver=webdriver.Chrome()
    yield driver
    driver.quit()
@pytest.mark.parametrize("username,password",read_credentials_from_csv("C://Users//ssekar588//PycharmProjects//GUVI Selenium 2//dframework//credential_data//credentials.csv"))
def test_login(browser,username,password):
    browser.get("https://www.saucedemo.com/")
    # login_test(browser,username,password)
    print(username,password)
    time.sleep(10)
    browser.find_element(by=By.ID,value="username").send_keys(username)
    browser.find_element(by=By.ID,value="password").send_keys(password)
    browser.find_element(by=By.ID,value="login_button").click()
    verify_ifloginsuccess(browser)
