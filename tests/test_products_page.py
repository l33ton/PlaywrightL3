
import pytest
from playwright.sync_api import expect
from constants import *

def test_add_item_to_shopping_cart(is_logged_in, products_page):
    products_page.add(products_page.ITEM_LOCATOR)
    expect(products_page.page.locator(SHOPPING_CART_BADGE_LOCATOR)).to_be_visible()

def test_remove_item_from_shopping_cart(is_logged_in, products_page):
    products_page.add(products_page.ITEM_LOCATOR)
    products_page.remove(products_page.ITEM_LOCATOR)
    expect(products_page.page.locator(SHOPPING_CART_BADGE_LOCATOR)).not_to_be_visible()

@pytest.mark.parametrize("item_number", range(6))
def test_if_information_of_all_the_products_is_shown(item_number, is_logged_in, products_page):
    products_page.show_information(item_number)
    expect(products_page.page.locator(BACK_TO_PRODUCTS_LOCATOR)).to_be_visible()
    expect(products_page.page.locator(ITEM_DESCRIPTION_LOCATOR)).to_be_visible()

def test_if_items_are_sorted_a_to_z(is_logged_in, products_page):
    products_page.sort_a_to_z()
    assert products_page.get_items() == products_page.sorted_a_to_z()

def test_if_items_are_sorted_z_to_a(is_logged_in, products_page):
    products_page.sort_z_to_a()
    assert products_page.get_items() == products_page.sorted_z_to_a()

def test_if_items_are_sorted_by_price_low_to_high(is_logged_in, products_page):
    products_page.sort_low_to_high_price()
    assert products_page.get_prices() == products_page.sorted_low_to_high_price()

def test_if_items_are_sorted_by_price_high_to_low(is_logged_in, products_page):
    products_page.sort_high_to_low_price()
    assert products_page.get_prices() == products_page.sorted_high_to_low_price()
