from Pages.BasePage import BasePage
from Locators.Locators import LoginPageLocators as lpl

class LoginPage(BasePage):
    def email_input_fill(self, email):
        self.driver.find_element(*lpl.login_page_email_input).send_keys(email)

    def password_input_fill(self, password):
        self.driver.find_element(*lpl.login_page_password_input).send_keys(password)

    def submit_button_click(self):
        self.driver.find_element(*lpl.login_page_submit_button).click()