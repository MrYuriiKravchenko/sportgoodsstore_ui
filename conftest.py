from selenium import webdriver
import pytest
from pages.search_products import SearchProduct
from pages.cart import Cart
from pages.category import Category
from pages.wishlist import WishList
from pages.pagination import PaginationPages


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    return chrome_driver

@pytest.fixture()
def search_product(driver):
    return SearchProduct(driver)

@pytest.fixture()
def cart(driver):
    return Cart(driver)

@pytest.fixture()
def category(driver):
    return Category(driver)

@pytest.fixture()
def wishlist(driver):
    return WishList(driver)

@pytest.fixture()
def pagination(driver):
    return PaginationPages(driver)

