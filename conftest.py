import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    url = "https://www.globalsqa.com/angularJs-protractor/BankingProject/"
    driver = webdriver.Firefox()
    driver.get(url)
    yield driver
    driver.close()
