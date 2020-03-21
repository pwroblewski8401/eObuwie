import unittest
from selenium import webdriver
import os
from Tests.SearchingAndProductsTests import SearchingAndProductsTests



def Runner(test_schema):
    #Test suits
    suit = unittest.TestSuite()
    for t in test_schema:
        suit.addTest(t)

    #runner
    runner = unittest.TextTestRunner(verbosity=1).run(suit)



