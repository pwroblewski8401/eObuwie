import unittest


def Runner(test_schema):
    #Test suits
    suit = unittest.TestSuite()
    for t in test_schema:
        suit.addTest(t)

    #runner
    runner = unittest.TextTestRunner(verbosity=1).run(suit)



