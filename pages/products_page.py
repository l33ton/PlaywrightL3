from constants import ITEM_LOCATOR, SORT_LOCATOR, PRICE_LOCATOR
from pages.base_page import BasePage


class ProductsPage(BasePage):
    ITEM_1_LOCATOR = "sauce-labs-backpack"
    ITEM_2_LOCATOR = "sauce-labs-bike-light"


    def __init__(self, page):
        super().__init__(page)

    def add(self, item):
        self.page.locator(f"[data-test='add-to-cart-{item}']").click()

    def remove(self, item):
        self.page.locator(f"[data-test='remove-{item}']").click()

    def show_information(self, item_number):
        self.page.locator(f"#item_{item_number}_title_link").click()

    def get_items(self):
        return self.page.locator(ITEM_LOCATOR).all_text_contents()

    def get_prices(self):
        prices = self.page.locator(PRICE_LOCATOR).all_text_contents()
        return [float(p.replace("$", "").strip()) for p in prices]

    def sort_a_to_z(self):
        self.page.locator(SORT_LOCATOR).select_option("az")

    def sort_z_to_a(self):
        self.page.locator(SORT_LOCATOR).select_option("za")

    def sort_low_to_high_price(self):
        self.page.locator(SORT_LOCATOR).select_option("lohi")

    def sort_high_to_low_price(self):
        self.page.locator(SORT_LOCATOR).select_option("hilo")

    def sorted_a_to_z(self):
        items = self.page.locator(ITEM_LOCATOR).all_text_contents()
        return sorted(items, key=lambda s: s.lower())

    def sorted_z_to_a(self):
        items = self.page.locator(ITEM_LOCATOR).all_text_contents()
        return sorted(items, key=lambda s: s.lower(), reverse=True)

    def sorted_low_to_high_price(self):
        return sorted(self.get_prices())

    def sorted_high_to_low_price(self):
        return sorted(self.get_prices(), reverse=True)
