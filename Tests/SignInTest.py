from Tests.TestBase import TestBase
from Pages.MainPage import MainPage
from Pages.SignInPage import SignInPage
from Pages.AccoutPage import AccountPage
from time import sleep


class SignInTest(TestBase):
    def test_signin_positive(self):
        print("INFO : This test is disabled - we don't want to create dummy accounts on the page!")
        # mp = MainPage(self.driver)
        # mp.signin_button_click()
        #
        # sip = SignInPage(self.driver)
        # sip.name_fill("Imie")
        # sip.last_name_fill("LastName")
        # sip.email_fill("MailTestowy1@email.com")
        # sip.password_fill("SupaZupa")
        # sip.password_confirmation_fill("SupaZupa")
        # sip.statement_checkbox_click()
        # sip.newsletter_checkbox_click()
        # sip.create_accout_button_click()
        #
        # ap = AccountPage(self.driver)
        # assert ap.h1_page_title_get() == 'Witaj, Imie!', "Account was not corretly created!"
        # print(ap.h1_page_title_get())
        # sleep(5)

    def test_signin_negative_wrong_email(self):
        mp = MainPage(self.driver)
        mp.signin_button_click()

        sip = SignInPage(self.driver)
        sip.name_fill("Imie")
        sip.last_name_fill("LastName")
        sip.email_fill("test")
        sip.password_fill("SupaZupa")
        sip.password_confirmation_fill("SupaZupa")
        sip.statement_checkbox_click()
        sip.create_accout_button_click()
        assert sip.get_email_error() == "Wprowadzono niepoprawny adres e-mail", "There is no email error!"

    def test_no_statement(self):
        mp = MainPage(self.driver)
        mp.signin_button_click()

        sip = SignInPage(self.driver)
        sip.name_fill("Name")
        sip.last_name_fill("LastName")
        sip.email_fill("email@email.com")
        sip.password_fill("SupaZupa")
        sip.password_confirmation_fill("SupaZupa")
        sip.newsletter_checkbox_click()
        sip.create_accout_button_click()
        assert self.UtilsSelenium.get_webpage_title() == "Utwórz nowe konto klienta | eobuwie.pl", f"Error: Page should be still on create account page and the title should be: Utwórz nowe konto klienta | eobuwie.pl, but it is {self.UtilsSelenium.get_webpage_title()} instead"

    def test_diff_passwords(self):
        mp = MainPage(self.driver)
        mp.signin_button_click()

        sip = SignInPage(self.driver)
        sip.name_fill("Name")
        sip.last_name_fill("LastName")
        sip.email_fill("email.test@wp.pl")
        sip.password_fill("SupaZupa")
        sip.password_confirmation_fill("ZupaSupa")
        sip.statement_checkbox_click()
        #sip.createAccoutButton_click()
        assert sip.is_visible_password_missmatch_error(), self.logger.error("Error: error is not visible!")
        assert sip.get_diff_password_error() == "Prosimy upewnić się, że hasła pasują do siebie.", self.logger.error("Error: There should be mismatch password error!")
        self.UtilsSelenium.takeScreenshot(self.testName)
