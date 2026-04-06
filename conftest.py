import pytest
from playwright.sync_api import Page

from pages.checkout_page import CheckoutPage
from pages.login_page import LoginPage
from pages.products_page import ProductsPage

@pytest.fixture
def credentials():
    return {
        "username": "standard_user",
        "password": "secret_sauce"
    }
@pytest.fixture
def mock_credentials():
    return {
        "username": "fake_user",
        "password": "fake_pass"
    }
@pytest.fixture
def checkout_information():
    return {
        "first_name": "Jake",
        "last_name": "Paul",
        "postal_code": "1111"
    }
@pytest.fixture
def login_page(page:Page, base_url):
    page.goto(base_url)
    return LoginPage(page)
@pytest.fixture
def products_page(page):
    return ProductsPage(page)
@pytest.fixture
def is_logged_in(login_page, credentials):
    login_page.login(credentials["username"], credentials["password"])
    return login_page
@pytest.fixture
def checkout_page(page):
    return CheckoutPage(page)
@pytest.fixture(params=[
    {"first_name": "Jake", "last_name": "Paul", "postal_code": ""},
    {"first_name": "", "last_name": "Paul", "postal_code": "1111"},
    {"first_name": "Jake", "last_name": "", "postal_code": "1111"},
    {"first_name": "", "last_name": "", "postal_code": ""}
])
def invalid_information(request):
    return request.param

@pytest.fixture
def finalize_order(products_page, checkout_information, checkout_page):
    products_page.add(products_page.ITEM_LOCATOR)
    checkout_page.navigate_to_checkout()
    checkout_page.fill_your_information(checkout_information["first_name"], checkout_information["last_name"],
                                        checkout_information["postal_code"])
    checkout_page.continue_to_finalize()

@pytest.fixture
def finalize_with_invalid_information(products_page, invalid_information, checkout_page):
    products_page.add(products_page.ITEM_LOCATOR)
    checkout_page.navigate_to_checkout()
    checkout_page.fill_your_information(
        invalid_information["first_name"],
        invalid_information["last_name"],
        invalid_information["postal_code"]
    )
    checkout_page.continue_to_finalize()