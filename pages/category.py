from pages.base_page import BasePage
from pages.locators import category_locators as loc

class Category(BasePage):
    page_url = ''

    def select_category(self):
        name_category = self.find(loc.category_name_locator)
        name_category.click()

    def check_category_results(self, execute_category):
        category_results = self.find(loc.category_results_locator)
        assert category_results.text == execute_category

