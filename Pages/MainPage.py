from Pages.BasePage import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Locators.Locators import MainPageLocators as mpl
from Locators.Locators import LoginPageLocators as lpl
from Locators.Locators import SignInLocators as sil

class MainPage(BasePage):
    def loginButton_click(self):
        self.driver.find_element(*mpl.main_page_login_button).click()
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(lpl.login_page_login_button))

    def signinButton_click(self):
        self.driver.find_element(*mpl.main_page_signin_button).click()
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(sil.signin_page_create_account_button))