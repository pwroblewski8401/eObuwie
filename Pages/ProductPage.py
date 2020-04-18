from Pages.BasePage import BasePage
from Locators.Locators import ProductPageLocators as ppl


class ProductPage(BasePage):
    def product_information_get(self, type):
        product_information_list = self.driver.find_elements(*ppl.product_page_list)
        for info in product_information_list:
            i = info.find_element(*ppl.product_page_information_label)
            d = info.find_element(*ppl.product_page_information_data)
            if type in i.text:
                return d.text