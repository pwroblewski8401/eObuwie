from Tests.TestBase import TestBase
from Pages.MainPage import MainPage
from Pages.LoginPage import LoginPage
from Pages.AccoutPage import AccountPage
from time import sleep


class LogInTest(TestBase):
    def test_LogIn_positive(self):
        mp = MainPage(self.driver)
        mp.login_button_click()

        lp = LoginPage(self.driver)
        lp.email_input_fill("MailTestowy1@email.com")
        lp.password_input_fill("SupaZupa")
        lp.submit_button_click()

        ap = AccountPage(self.driver)
        self.assertEqual(ap.h1_page_title_get(), 'Witaj, Imie!', "Account was not corretly created!")
        sleep(5)
