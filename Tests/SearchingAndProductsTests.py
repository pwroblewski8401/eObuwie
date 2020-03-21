from Pages.MainPage import MainPage
from Tests.TestBase import TestBase
from Pages.SearchPage import SearchPage
from Pages.ProductPage import  ProductPage
from time import sleep



class SearchingAndProductsTests(TestBase):
    def test_search(self):
        search_sentence = "Addidas campus"
        mp = MainPage(self.driver)
        mp.searchboxInput_fill(search_sentence)

        sp = SearchPage(self.driver)
        search_result = sp.h1_pageTitle_text_get()
        self.UtilsSelenium.take_screenshot(self.testName)
        assert 'Wyniki wyszukiwania dla Addidas campus' in search_result, self.logger.error(f'Searching test fail for: {search_sentence}!')

class SearchingAndProductsCardsTest(TestBase):
    def test_product_card(self):
        search_sentence = "Addidas campus"
        product = "Campus W DB3277"
        mp = MainPage(self.driver)
        mp.searchboxInput_fill(search_sentence)

        sp = SearchPage(self.driver)
        self.logger.info(f"Found product {sp.search_count_get()}")
        sp.search_page_product_bySecondName_click(product)

        pp = ProductPage(self.driver)
        data = pp.product_information_get('Model:')
        print(f"Data to search: {data}")
        assert product in data, self.logger.error(f"Wrong product selected! Should be {product} is: {data}")
        self.UtilsSelenium.take_screenshot(self.testName)


