from Pages.MainPage import MainPage
from Tests.TestBase import TestBase
from Pages.SearchPage import SearchPage
from Pages.ProductPage import ProductPage
from time import sleep


class SearchingAndProductsTests(TestBase):
    def test_search(self):
        search_sentence = "Addidas campus"
        mp = MainPage(self.driver)
        mp.searchbox_input_fill(search_sentence, True)

        sp = SearchPage(self.driver)
        search_result = sp.h1_page_title_text_get()
        self.UtilsSelenium.takeScreenshot(self.testName)
        assert 'Wyniki wyszukiwania dla Addidas campus' in search_result, self.logger.error(f'Searching test fail for: {search_sentence}!')


class SearchingAndProductsCardsTest(TestBase):
    def test_product_card(self):
        search_sentence = "Addidas campus"
        product = "Campus W DB3277"
        mp = MainPage(self.driver)
        mp.searchbox_input_fill(search_sentence)

        sp = SearchPage(self.driver)
        self.logger.info(f"Found product {sp.search_count_get()}")
        sp.search_page_product_by_second_name_click(product)

        pp = ProductPage(self.driver)
        data = pp.product_information_get('Model:')
        print(f"Data to search: {data}")
        assert product in data, self.logger.error(f"Wrong product selected! Should be {product} is: {data}")
        self.UtilsSelenium.takeScreenshot(self.testName)


class SearchingAndProductsCardsTestList(TestBase):
    def test_search_list(self):
        search_sentence = "Nike airmax"
        mp = MainPage(self.driver)
        mp.searchbox_input_fill(search_sentence, False)
        sleep(5)
        product_list = mp.get_quick_procucts_list()
        product_name = mp.quick_search_list_select_index(2, product_list)
        pp = ProductPage(self.driver)
        name_on_product_card = pp.product_information_get("Model:")
        self.assertIn(name_on_product_card, product_name, f'{product_name} not in {name_on_product_card}')
        sleep(5)



