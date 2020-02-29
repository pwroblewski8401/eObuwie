from Pages.MainPage import MainPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Locators.Locators import MyAccountLocators as mal

class AccountPage(MainPage):
    def h1_pageTitle_get(self):
        return self.driver.find_element(*mal.myaccount_page_title_div).text