def test_category_menu(category):
    category.open_page()
    category.select_category()
    category.check_category_results('Велосипеды')
