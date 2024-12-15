from pages.base_page import BasePage
from pages.locators import pagination_locators as loc

class PaginationPages(BasePage):
    page_url = ''

    def pagination_page(self):
        button_pagination = self.find(loc.button_pagination_locator)
        button_pagination.click()

    def check_for_button_presence_back(self, button):
        button_back = self.find(loc.button_back_locator)
        assert button_back.text == button