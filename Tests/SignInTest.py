from Tests.TestBase import TestBase
from Pages.MainPage import MainPage
from Pages.SignInPage import SignInPage
from Pages.AccoutPage import AccountPage
from time import sleep

class SignInTest(TestBase):
    def test_signin_positive(self):
        mp = MainPage(self.driver)
        mp.signinButton_click()

        sip = SignInPage(self.driver)
        sip.name_fill("Imie")
        sip.lastName_fill("LastName")
        sip.email_fill("MailTestowy@email.com")
        sip.password_fill("SupaZupa")
        sip.passswordConfirmation_fill("SupaZupa")
        sip.statementCheckBox_click()
        sip.newsletterCheckBox_click()
        sip.createAccoutButton_click()

        ap = AccountPage(self.driver)
        assert ap.h1_pageTitle_get() == 'Witaj, Imie!', "Account was not corretly created!"
        print(ap.h1_pageTitle_get())
        sleep(10)

    def test_signin_negative_wrong_email(self):
        mp = MainPage(self.driver)
        mp.signinButton_click()

        sip = SignInPage(self.driver)
        sip.name_fill("Imie")
        sip.lastName_fill("LastName")
        sip.email_fill("test")
        sip.password_fill("SupaZupa")
        sip.passswordConfirmation_fill("SupaZupa")
        sip.statementCheckBox_click()
        sip.createAccoutButton_click()
        assert sip.getEmailError() == "Wprowadzono niepoprawny adres e-mail", "There is no email error!"

    def test_no_statement(self):
        mp = MainPage(self.driver)
        mp.signinButton_click()

        sip = SignInPage(self.driver)
        sip.name_fill("Name")
        sip.lastName_fill("LastName")
        sip.email_fill("email@email.com")
        sip.password_fill("SupaZupa")
        sip.passswordConfirmation_fill("SupaZupa")
        sip.newsletterCheckBox_click()
        sip.createAccoutButton_click()
        assert self.UtilsSelenium.get_webpage_title() == "Utwórz nowe konto klienta | eobuwie.pl", f"Error: Page should be still on create account page and the title should be: Utwórz nowe konto klienta | eobuwie.pl, but it is {self.UtilsSelenium.get_webpage_title()} instead"

    def test_diff_passwords(self):
        mp = MainPage(self.driver)
        mp.signinButton_click()

        sip = SignInPage(self.driver)
        sip.name_fill("Name")
        sip.lastName_fill("LastName")
        sip.email_fill("email.test@wp.pl")
        sip.password_fill("SupaZupa")
        sip.passswordConfirmation_fill("ZupaSupa")
        sip.statementCheckBox_click()
        sip.createAccoutButton_click()
        assert sip.isVisiblePasswordMissmatchError(), "Error: error is not vivible!"
        assert sip.getDiffPasswordsError() == "Prosimy upewnić się, że hasła pasują do siebie.", "Error: There should be mismatch password error!"
        self.UtilsSelenium.make_screenshot(self.name)
