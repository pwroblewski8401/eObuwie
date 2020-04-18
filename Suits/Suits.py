from Tests.SearchingAndProductsTests import SearchingAndProductsTests
from Tests.SearchingAndProductsTests import SearchingAndProductsCardsTest
from Tests.SearchingAndProductsTests import SearchingAndProductsCardsTestList
from Tests.SignInTest import SignInTest

import unittest


class TestSuits:
    def __init__(self):
        self.signInTest = unittest.TestLoader().loadTestsFromTestCase(SignInTest)
        print(self.signInTest)
        self.searchProductTest = unittest.TestLoader().loadTestsFromTestCase(SearchingAndProductsTests)
        self.searchProductCardTest = unittest.TestLoader().loadTestsFromTestCase(SearchingAndProductsCardsTest)
        self.searchProductCardQuickSearchTest = unittest.TestLoader().loadTestsFromTestCase(SearchingAndProductsCardsTestList)

    def all_tests(self):
        tests_list = [self.signInTest, self.searchProductTest, self.searchProductCardTest, self.searchProductCardQuickSearchTest]
        return tests_list

    def signin_tests(self):
        print(self.signInTest)
        test_list = [self.signInTest]
        return test_list

    def search_tests(self):
        test_list = [self.searchProductCardTest, self.searchProductTest, self.searchProductCardQuickSearchTest]
        return test_list
