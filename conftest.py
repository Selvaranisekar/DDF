import pytest
from selenium import webdriver
@pytest.fixture(scope="session")
def browser():
    driver=webdriver.chrome()
    yield driver
    driver.quit()