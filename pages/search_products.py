from pages.base_page import BasePage
from pages.locators import search_locators as loc

class SearchProduct(BasePage):
    page_url = ""

    def search_form(self, product):
        form_field = self.find(loc.search_field_locator)
        button = self.find(loc.button_locator)
        form_field.send_keys(product)
        button.click()

    def check_found_product(self, product_results):
        results_found = self.find(loc.results_found_locator)
        assert results_found.text == product_results

