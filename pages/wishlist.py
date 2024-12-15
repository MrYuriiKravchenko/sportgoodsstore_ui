from pages.base_page import BasePage
from pages.locators import wishlist_locators as loc

class WishList(BasePage):
    page_url = ''

    def wishlist_add_product(self):
        button = self.find(loc.button_wishlist_locator)
        button.click()

    def check_what_redirects_to_authorization(self, text_authorization):
        authorization = self.find(loc.authorization_locator)
        assert authorization.text == text_authorization

