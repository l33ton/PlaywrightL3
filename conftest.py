import pytest
from playwright.sync_api import Page

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
def login_page(page:Page, base_url):
    page.goto(base_url)
    return LoginPage(page)
@pytest.fixture
def products_page(is_logged_in):
    return ProductsPage(is_logged_in.page)
@pytest.fixture
def is_logged_in(login_page, credentials):
    login_page.login(credentials["username"], credentials["password"])
    return login_page
