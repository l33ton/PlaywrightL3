from playwright.sync_api import expect
from constants import *


def test_login_with_valid_credentials(is_logged_in, base_url):
    expect(is_logged_in.page).to_have_url(f"{base_url}{INVENTORY_URL}")
    expect(is_logged_in.page.locator(SHOPPING_CART_LOCATOR)).to_be_visible()

def test_login_with_invalid_credentials(login_page, mock_credentials):
    login_page.login(mock_credentials["username"], mock_credentials["password"])
    error = login_page.page.locator(ERROR_MESSAGE_LOCATOR)
    expect(error).to_be_visible()
    expect(error).to_contain_text(ERROR_MESSAGE)

def test_login_without_credentials(login_page):
    login_page.submit()
    error = login_page.page.locator(ERROR_MESSAGE_LOCATOR)
    expect(error).to_be_visible()
    expect(error).to_contain_text(USERNAME_REQUIRED_MESSAGE)

def test_login_without_password(login_page, credentials):
    login_page.login(credentials["username"], "")
    error = login_page.page.locator(ERROR_MESSAGE_LOCATOR)
    expect(error).to_be_visible()
    expect(error).to_contain_text(PASSWORD_REQUIRED_MESSAGE)

def test_login_without_username(login_page, credentials):
    login_page.login("", credentials["password"])
    error = login_page.page.locator(ERROR_MESSAGE_LOCATOR)
    expect(error).to_be_visible()
    expect(error).to_contain_text(USERNAME_REQUIRED_MESSAGE)

def test_if_password_input_is_hidden(login_page, credentials):
    password = login_page.page.locator(PASSWORD_LOCATOR)
    expect(password).to_have_attribute("type", "password")

def test_login_with_sql_injection(login_page, mock_credentials):
    login_page.login(SQL_INJECTION_INPUT, mock_credentials["password"])
    error = login_page.page.locator(ERROR_MESSAGE_LOCATOR)
    expect(error).to_be_visible()
    expect(error).to_contain_text(ERROR_MESSAGE)