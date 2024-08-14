import unittest


class SignUpTest(unittest.TestCase):
    def test_signUp_by_eamil(self):
        print('test_signUp_by_eamil')
        self.assertTrue(True)

    def test_signUp_by_facebook(self):
        print('test_signUp_by_facebook')
        self.assertTrue(True)

    def test_signUp_by_twitter(self):
        print('test_signUp_by_twitter')
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()
