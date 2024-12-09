from selenium import webdriver
import pytest
from pages.search_products import SearchProduct


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    return chrome_driver

@pytest.fixture()
def search_product(driver):
    return SearchProduct(driver)

