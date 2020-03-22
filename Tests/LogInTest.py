from Tests.TestBase import TestBase
from Pages.MainPage import MainPage
from Pages.LoginPage import LoginPage
from Pages.AccoutPage import AccountPage
from time import sleep

class LogInTest(TestBase):
    def test_LogIn_positive(self):
        mp = MainPage(self.driver)
        mp.loginButton_click()

        lp = LoginPage(self.driver)
        lp.emailInput_fill("MailTestowy1@email.com")
        lp.passwordInput_fill("SupaZupa")
        lp.subbmitButton_clik()

        ap = AccountPage(self.driver)
        self.assertEqual(ap.h1_pageTitle_get(), 'Witaj, Imie!', "Account was not corretly created!")
        sleep(5)
