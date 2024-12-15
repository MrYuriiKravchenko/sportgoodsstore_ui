def test_pagination(pagination):
    pagination.open_page()
    pagination.pagination_page()
    pagination.check_for_button_presence_back('<')

