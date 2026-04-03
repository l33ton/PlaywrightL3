from constants import PASSWORD_LOCATOR, USERNAME_LOCATOR, SUBMIT_BUTTON_LOCATOR
from pages.base_page import BasePage


class LoginPage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.username_input = page.locator(USERNAME_LOCATOR)
        self.password_input = page.locator(PASSWORD_LOCATOR)
        self.submit_button = page.locator(SUBMIT_BUTTON_LOCATOR)

    def login(self, username, password):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.submit_button.click()

    def submit(self):
        self.submit_button.click()