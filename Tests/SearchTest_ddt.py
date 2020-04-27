from Pages.MainPage import MainPage
from Tests.TestBase import TestBase
from Pages.SearchPage import SearchPage
from Pages.CartPage import CartPage
from Pages.ProductPage import ProductPage
from time import sleep
from ddt import ddt, data, file_data, unpack


def read_product_form_txt_file(file_name):
    product_list = []
    file = open(file_name, "r")
    lines = file.readlines()
    for line in lines:
        product_in_line = []
        split = line.split(',')
        for s in split:
            s = s.replace("\n", '')
            product_in_line.append(s)
        product_list.append(product_in_line)
    print(product_list)
    return product_list


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

    @data(*read_product_form_txt_file('test_data_long_test.txt'))
    @unpack
    def test_add_multiple_product_to_basket(self, *procuct_list):
        print(procuct_list)
        mp = MainPage(self.driver)
        pp = ProductPage(self.driver)
        product_added_to_basket = []
        for product in procuct_list:
            mp.searchbox_input_fill(product, False)
            sleep(2)
            list = mp.get_quick_procucts_list()
            mp.quick_search_list_select_index(0, list)
            if pp.get_availability():
                if pp.if_size_selector_is_presence():
                    pp.get_sizes()
                pp.add_to_basket()
                selected_product = pp.product_information_get('Model:')
                pp.close_basket_popup_window()
                pp.get_back_to_main_page()
                product_added_to_basket.append(selected_product)
            else:
                print(f"Product {product} is not available. Skipping!")
        mp.button_cart_click()
        cp = CartPage(self.driver)
        product_in_cart = cp.get_products_in_cart()
        check = True
        for product in product_added_to_basket:
            partial_check = False
            for prduct_cart in product_in_cart:
                if product in prduct_cart:
                    partial_check = True
            if not partial_check:
                print(f"Product {product} should be in cart, but it is not! Cart contains: {product_in_cart}")
                check = False

        self.assertEqual(check, True)




