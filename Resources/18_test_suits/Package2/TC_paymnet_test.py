import unittest

class paymnetTest(unittest.TestCase):
    def test_paymnet_in_dollor(self):
        print("This is paymeny in dollor test")
        self.assertTrue(True)

    def test_paymnet_in_rupess(self):
        print("This is paymeny in rupess test")
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()