import unittest


class LoginTest(unittest.TestCase):
    def test_login_by_eamil(self):
        print('test_login_by_eamil')
        self.assertTrue(True)

    def test_login_by_facebook(self):
        print('test_login_by_facebook')
        self.assertTrue(True)

    def test_login_by_twitter(self):
        print('test_login_by_twitter')
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()
