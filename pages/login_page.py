from pages.base_page import BasePage


class LoginPage(BasePage):
    URL = "https://default.web-dev1.avallainmagnet.com/"

    # locators
    EMAIL_INPUT = "#login-email"
    PASSWORD_INPUT = "#login-password"
    PASSWORD_INPUT = "#login-password"
    SUBMIT_BUTTON = "button[type='submit']"

    def open(self):
        self.navigate(self.URL)
        self.page.wait_for_load_state("networkidle")

    def login(self, email: str, password: str):
        self.page.fill(self.EMAIL_INPUT, email)
        self.page.fill(self.PASSWORD_INPUT, password)
        self.page.locator(self.SUBMIT_BUTTON).click()
        self.page.wait_for_timeout(4000)
