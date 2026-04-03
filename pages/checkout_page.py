from constants import CHECKOUT_LOCATOR, FIRST_NAME_LOCATOR, LAST_NAME_LOCATOR, POSTAL_CODE_LOCATOR, \
    CONTINUE_BUTTON_LOCATOR, FINISH_BUTTON_LOCATOR, SHOPPING_CART_LOCATOR
from pages.base_page import BasePage

class CheckoutPage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.checkout_button = self.page.locator(CHECKOUT_LOCATOR)
        self.first_name_input = self.page.locator(FIRST_NAME_LOCATOR)
        self.last_name_input = self.page.locator(LAST_NAME_LOCATOR)
        self.postal_code_input = self.page.locator(POSTAL_CODE_LOCATOR)
        self.continue_checkout_button = self.page.locator(CONTINUE_BUTTON_LOCATOR)
        self.finish_checkout_button = self.page.locator(FINISH_BUTTON_LOCATOR)

    def navigate_to_checkout(self):
        return self.page.locator(SHOPPING_CART_LOCATOR).click()

    def fill_your_information(self, first_name, last_name, postal_code):
        self.checkout_button.click()
        self.first_name_input.fill(first_name)
        self.last_name_input.fill(last_name)
        self.postal_code_input.fill(postal_code)

    def continue_to_finalize(self):
        self.continue_checkout_button.click()

    def finish(self):
        self.finish_checkout_button.click()
