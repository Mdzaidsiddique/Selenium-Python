import unittest

"""
setup:              executes multiple times before completion of every test methods
teardown:           executes multiple times after completion of every test methods
setUpClass:         executes one times before actual test methods are started
tearDownClass:      executes one times after completion of all test methods

below method are module level, outside class
setUpModule:        
tearDownModule:
"""

def setup_module():
    print("setup_module")

def teardown_module():
    print("teardown_module")
class AppTesting(unittest.TestCase):

    @classmethod
    def setUp(self): # this method will execute before every test methods
        print('Login ----- setup method')
    @classmethod
    def tearDown(self): print('logout-----teardown method')  #after every test method

    @classmethod
    def setUpClass(cls):
        print('welcome ----- setUpClass')

    @classmethod
    def tearDownClass(cls):
        print('bye bye ----- tearDownClass')
    def test_search(self):
        print("this is test search")

    def test_advance_search(self):
        print("this is test advance search")
    def test_prepaid_recharge(self):
        print("this is test prepare recharge")

    def test_postpaid_recharge(self):
        print("this is test postpause recharge")



if __name__ == '__main__':
    unittest.main()

