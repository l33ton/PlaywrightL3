def test_checkout_information(is_logged_in, checkout_page, products_page, checkout_information):
    products_page.add(products_page.ITEM_1_LOCATOR)
    checkout_page.navigate_to_checkout()
    checkout_page.fill_your_information(checkout_information["first_name"], checkout_information["last_name"], checkout_information["postal_code"])
    checkout_page.finish_your_order()