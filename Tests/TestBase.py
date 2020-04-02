from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Locators.Locators import MainPageLocators as mpl
from Utils.UtilsSelenium import UtilsSelenium
from Utils.Logger import Logger
import unittest
import time

class TestBase(unittest.TestCase):
    def setUp(self) -> None:
        self.testName = unittest.TestCase.id(self)
        self.logger = Logger(self.testName)
        if not self.logger:
            self.fail("No logger!")
        self.logger.info("Test started!")
        self.driver = webdriver.Chrome()
        self.UtilsSelenium = UtilsSelenium(self.driver, self.logger)
        self.driver.get("https://www.eobuwie.com.pl/")
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(mpl.main_page_login_button))
        self.driver.maximize_window()
        #assert self.driver.title == "Modne buty damskie, męskie, dziecięce oraz torebki  | eobuwie.pl", f"Loaded page in not main page. Title is {self.driver.title} and should be Modne buty damskie, męskie, dziecięce oraz torebki  | eobuwie.pl"
        accept_cookies_button = self.driver.find_element(*mpl.main_page_cookies_accept_button)
        accept_cookies_close_button = self.driver.find_element(*mpl.main_page_cookies_close_button)
        if(accept_cookies_button.is_displayed()):
            accept_cookies_close_button.click()

    def tearDown(self) -> None:
        self.logger.info(f"Test runner finished!")
        self.driver.quit()