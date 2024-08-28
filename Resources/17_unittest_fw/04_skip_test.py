import unittest

class AppTest(unittest.TestCase):
    @unittest.SkipTest
    def test_search1(self):
        print("this is search test 1")

    # skip by reason
    @unittest.skip("I am skipping this test method because it is not yet ready")
    def test_search2(self):
        print("this is search test 2")

    @unittest.skipIf(1==1, "One is equal to one")
    def test_search_3(self):
        print("this is search test 3")

    def test_search_4(self):
        print("this is search test 4")

    def test_search_5(self):
        print("this is search test 5")

    def test_search_6(self):
        print("this is search test 6")

if __name__ == '__main__':
    unittest.main()