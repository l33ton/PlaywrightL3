from playwright.sync_api import expect

from constants import FINISH_BUTTON_LOCATOR, ORDER_INFO_LOCATOR, ORDER_CONFIRMATION_MESSAGE, ERROR_MESSAGE_LOCATOR


def test_if_checkout_information_is_shown(finalize_order, checkout_page):

    expect(checkout_page.page.locator(ORDER_INFO_LOCATOR)).to_be_visible()
    expect(checkout_page.page.locator(FINISH_BUTTON_LOCATOR)).to_be_visible()

def test_if_order_is_done(finalize_order, checkout_page):
    checkout_page.finish()

    expect(checkout_page.page.get_by_text(ORDER_CONFIRMATION_MESSAGE)).to_be_visible()

def test_checkout_with_missing_information(finalize_with_invalid_information, checkout_page):

    expect(checkout_page.page.locator(ERROR_MESSAGE_LOCATOR)).to_be_visible()
