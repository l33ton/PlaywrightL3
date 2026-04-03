class BasePage:

    def __init__(self, page):
        self.page = page

    def navigate(self, base_url):
        self.page.goto(base_url)