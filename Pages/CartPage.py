from Pages.BasePage import BasePage
from Locators.Locators import CartPageLocators as cpl
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage(BasePage):
    def get_products_in_cart(self):
        basket = self.driver.find_element(*cpl.cart_page_product_in_cart)
        products_models_in_cart = basket.find_elements(*cpl.cart_page_product_model_in_cart)
        products = []
        for product in products_models_in_cart:
            products.append(product.text)
        return products

