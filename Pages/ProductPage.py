from Pages.BasePage import BasePage
from Locators.Locators import ProductPageLocators as ppl
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Locators.Locators import MainPageLocators as mpl


class ProductPage(BasePage):
    def product_information_get(self, type):
        product_information_list = self.driver.find_elements(*ppl.product_page_list)
        for info in product_information_list:
            i = info.find_element(*ppl.product_page_information_label)
            d = info.find_element(*ppl.product_page_information_data)
            if type in i.text:
                return d.text

    def get_back_to_main_page(self):
        self.driver.get("https://www.eobuwie.com.pl/")
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(mpl.main_page_login_button))

    def close_basket_popup_window(self):
        close_button = self.driver.find_element(*ppl.product_page_close_basket_popup_button)
        if close_button.is_displayed():
            close_button.click()

    def add_to_basket(self):
        add_button = self.driver.find_element(*ppl.product_page_add_to_cart)
        add_button.click()
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(ppl.product_page_close_basket_popup_button))

    def if_size_selector_is_presence(self):
        try:
            size_selector = self.driver.find_element(*ppl.product_page_size_selector)
            if(size_selector.is_displayed()):
                return True
            else:
                return False
        except Exception:
            return False

    def get_sizes(self):
        self.driver.find_element(*ppl.product_page_size_selector).click()
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(ppl.product_page_sizes_ul))
        sizes = self.driver.find_elements(*ppl.product_page_sizes)
        sizes[0].click()

    def get_availability(self):
        availability = self.driver.find_element(*ppl.product_page_availability)
        if(availability.text== "Produkt niedostępny"):
            return False
        else:
            return True




