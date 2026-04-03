from playwright.sync_api import expect

from constants import FINISH_BUTTON_LOCATOR, ORDER_INFO_LOCATOR, ORDER_CONFIRMATION_MESSAGE, ERROR_MESSAGE_LOCATOR


def test_if_checkout_information_is_shown(is_logged_in, checkout_page, products_page, checkout_information):
    products_page.add(products_page.ITEM_1_LOCATOR)
    checkout_page.navigate_to_checkout()
    checkout_page.fill_your_information(checkout_information["first_name"], checkout_information["last_name"], checkout_information["postal_code"])
    checkout_page.continue_to_finalize()

    expect(checkout_page.page.locator(ORDER_INFO_LOCATOR)).to_be_visible()
    expect(checkout_page.page.locator(FINISH_BUTTON_LOCATOR)).to_be_visible()

def test_if_order_is_done(is_logged_in, checkout_page, products_page, checkout_information):
    products_page.add(products_page.ITEM_1_LOCATOR)
    checkout_page.navigate_to_checkout()
    checkout_page.fill_your_information(checkout_information["first_name"], checkout_information["last_name"], checkout_information["postal_code"])
    checkout_page.continue_to_finalize()
    checkout_page.finish()

    expect(checkout_page.page.get_by_text(ORDER_CONFIRMATION_MESSAGE)).to_be_visible()

def test_checkout_with_missing_information(is_logged_in, checkout_page, products_page, invalid_information):
    products_page.add(products_page.ITEM_1_LOCATOR)
    checkout_page.navigate_to_checkout()
    checkout_page.fill_your_information(
        invalid_information["first_name"],
        invalid_information["last_name"],
        invalid_information["postal_code"]
    )
    checkout_page.continue_to_finalize()

    expect(checkout_page.page.locator(ERROR_MESSAGE_LOCATOR)).to_be_visible()
