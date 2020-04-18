from Pages.MainPage import MainPage
from Tests.TestBase import TestBase
from Pages.SearchPage import SearchPage
from Pages.ProductPage import ProductPage
from time import sleep
from ddt import ddt, data, file_data, unpack


@ddt
class SearchingAndProductsCardsTestList(TestBase):
    @data("Nike airmax", "Addidas campus")
    def test_search_list(self, product):
        search_sentence = product
        mp = MainPage(self.driver)
        mp.searchbox_input_fill(search_sentence, False)
        sleep(5)
        product_list = mp.get_quick_procucts_list()
        product_name = mp.quick_search_list_select_index(2, product_list)
        pp = ProductPage(self.driver)
        name_on_product_card = pp.product_information_get("Model:")
        self.assertIn(name_on_product_card, product_name, f'{product_name} not in {name_on_product_card}')
        sleep(5)



