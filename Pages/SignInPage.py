from Pages.BasePage import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Locators.Locators import SignInLocators as sil


class SignInPage(BasePage):
    def name_fill(self, name):
        self.driver.find_element(*sil.signin_page_name_input).send_keys(name)

    def lastName_fill(self, lastname):
        self.driver.find_element(*sil.signin_page_last_name_input).send_keys(lastname)

    def email_fill(self, email):
        self.driver.find_element(*sil.signin_page_email_input).send_keys(email)

    def password_fill(self, password):
        self.driver.find_element(*sil.signin_page_password_input).send_keys(password)

    def passswordConfirmation_fill(self, password):
        self.driver.find_element(*sil.signin_page_password_confirm_input).send_keys(password)

    def statementCheckBox_click(self):
        self.driver.find_element(*sil.singin_page_statement_checkbox).click()

    def newsletterCheckBox_click(self):
        self.driver.find_element(*sil.signin_page_newsletter_checkbox).click()

    def createAccoutButton_click(self):
        self.driver.find_element(*sil.signin_page_create_account_button).click()

    def getAllErrorsTexts(self):
        errors = []
        errs = self.driver.find_elements(*sil.signin_page_errors_locator)
        for error in errs:
            errors.append(error.text)
        return errors

    def getEmailError(self):
        return self.driver.find_element(*sil.signin_page_email_input).find_element(*sil.signin_page_errors_locator).text

    def getDiffPasswordsError(self):
        return self.driver.find_element(*sil.signin_page_email_input).find_element(*sil.signin_page_errors_locator).text

    def isVisiblePasswordMissmatchError(self):
        return self.driver.find_element(*sil.signin_page_email_input).find_element(*sil.signin_page_errors_locator).is_displayed()


