from Pages.BasePage import BasePage
from Locators.Locators import MyAccountLocators as mal

class AccountPage(BasePage):
    def h1_pageTitle_get(self):
        return self.driver.find_element(*mal.myaccount_page_title_div).text