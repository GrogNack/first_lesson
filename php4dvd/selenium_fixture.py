from selenium import webdriver
import pytest

@test.fixture
def driver(request):
    driver = webdriver.Firefox()
    driver.implicitly_wait(10)
    request.addfinallizer(driver.quit)
    return driver
