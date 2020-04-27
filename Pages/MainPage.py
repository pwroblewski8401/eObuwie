from Pages.BasePage import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from Locators.Locators import MainPageLocators as mpl
from Locators.Locators import LoginPageLocators as lpl
from Locators.Locators import SignInLocators as sil
from Locators.Locators import ProductPageLocators as ppl
from Locators.Locators import CartPageLocators as cpl


class MainPage(BasePage):
    def login_button_click(self):
        self.driver.find_element(*mpl.main_page_login_button).click()
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(lpl.login_page_login_button))

    def signin_button_click(self):
        self.driver.find_element(*mpl.main_page_signin_button).click()
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(sil.signin_page_create_account_button))

    def searchbox_input_fill(self, search_text, click_enter):
        search_input = self.driver.find_element(*mpl.main_page_search_input)
        search_input.send_keys(search_text)
        if click_enter:
            search_input.send_keys(Keys.ENTER)
        else:
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(mpl.main_page_search_quickList))

    def get_quick_procucts_list(self):
        list = self.driver.find_elements(*mpl.main_page_search_productsFormQuickList)
        return list

    def quick_search_list_select_index(self, index, list):
        el = list[index]
        name = el.find_element(*mpl.main_page_search_productsFormQuickListSecondName).text
        el.click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(ppl.product_page_product_link))
        return name

    def quick_search_get_name_from_index(self, index, list):
        e = list[index]
        return e.find_element(*mpl.main_page_search_productsFormQuickListSecondName).text

    def button_cart_click(self):
        cart_button = self.driver.find_element(*mpl.main_page_cart_button)
        cart_button.click()
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(mpl.main_page_see_cart_button))
        see_cart_button = self.driver.find_element(*mpl.main_page_see_cart_button)
        see_cart_button.click()
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(cpl.cart_page_product_in_cart))

