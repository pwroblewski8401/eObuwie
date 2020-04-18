from Pages.BasePage import BasePage
from Locators.Locators import SignInLocators as sil


class SignInPage(BasePage):
    def name_fill(self, name):
        self.driver.find_element(*sil.signin_page_name_input).send_keys(name)

    def last_name_fill(self, lastname):
        self.driver.find_element(*sil.signin_page_last_name_input).send_keys(lastname)

    def email_fill(self, email):
        self.driver.find_element(*sil.signin_page_email_input).send_keys(email)

    def password_fill(self, password):
        self.driver.find_element(*sil.signin_page_password_input).send_keys(password)

    def password_confirmation_fill(self, password):
        self.driver.find_element(*sil.signin_page_password_confirm_input).send_keys(password)

    def statement_checkbox_click(self):
        self.driver.find_element(*sil.singin_page_statement_checkbox).click()

    def newsletter_checkbox_click(self):
        self.driver.find_element(*sil.signin_page_newsletter_checkbox).click()

    def create_accout_button_click(self):
        self.driver.find_element(*sil.signin_page_create_account_button).click()

    def get_all_errors_texts(self):
        errors = []
        errs = self.driver.find_elements(*sil.signin_page_errors_locator)
        for error in errs:
            errors.append(error.text)
        return errors

    def get_email_error(self):
        return self.driver.find_element(*sil.signin_page_email_input).find_element(*sil.signin_page_errors_locator).text

    def get_diff_password_error(self):
        return self.driver.find_element(*sil.signin_page_email_input).find_element(*sil.signin_page_errors_locator).text

    def is_visible_password_missmatch_error(self):
        try:
            return self.driver.find_element(*sil.signin_page_email_input).find_element(
                *sil.signin_page_errors_locator).is_displayed()
        except:
            return False
