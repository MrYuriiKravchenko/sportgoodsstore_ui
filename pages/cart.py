from pages.base_page import BasePage
from pages.locators import cart_locators as loc

class Cart(BasePage):
    page_url = '/28/krossovki-bug/'

    def cart_add_product(self):
        button = self.find(loc.button_add_to_cart_locator)
        button.click()

    def check_name_product(self, expected_product):
        name_product = self.find(loc.name_product_locator)
        assert name_product.text == expected_product

    def check_indicator(self, expected_number):
        indicator_num = self.find(loc.indicator_nuber_locator)
        assert int(indicator_num.text) == expected_number


