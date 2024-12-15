def test_wishlist_add_product(wishlist):
    wishlist.open_page()
    wishlist.wishlist_add_product()
    wishlist.check_what_redirects_to_authorization('ВХОД')