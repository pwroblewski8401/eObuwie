from Locators.Locators import SearchPageLocators as spl
from Locators.Locators import ProductPageLocators as ppl
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Pages.BasePage import BasePage


class SearchPage(BasePage):
    def h1_page_title_text_get(self):
        return self.driver.find_element(*spl.search_page_h1).text

    def search_count_get(self):
        return len(self.driver.find_elements(*spl.search_page_searched_products))

    def search_page_product_by_second_name_click(self, second_name):
        products_second_names = self.driver.find_elements(*spl.search_page_searched_product_second_names)
        for name in products_second_names:
            if second_name in name.text:
                name.click()
                break
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(ppl.product_page_product_link))