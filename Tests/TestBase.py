from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Locators.Locators import MainPageLocators as mpl
from Utils.UtilsSelenium import UtilsSelenium
import unittest

class TestBase(unittest.TestCase):
    def setUp(self) -> None:
        self.name = unittest.TestCase.id(self)
        self.driver = webdriver.Chrome()
        self.UtilsSelenium = UtilsSelenium(self.driver)
        self.driver.get("https://www.eobuwie.com.pl/")
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(mpl.main_page_login_button))
        self.driver.maximize_window()
        #assert self.driver.title == "Modne buty damskie, męskie, dziecięce oraz torebki  | eobuwie.pl", f"Loaded page in not main page. Title is {self.driver.title} and should be Modne buty damskie, męskie, dziecięce oraz torebki  | eobuwie.pl"
        accept_cookies_button = self.driver.find_element(*mpl.main_page_cookies_accept_button)
        if(accept_cookies_button.is_displayed()):
            accept_cookies_button.click()

    def tearDown(self) -> None:
        self.driver.quit()