import unittest
from selenium import webdriver
# 05_unit_test_assertions.py

# assertEqual: compare first parameter with second if both equal then run else fail

# assertNotEqual: opposite of assertEqual

# assertTrue: if we have more than two parameter, it checks weather given parameter is true or not, if true then pass else fail

# assertFalse: compares weather given values or expression is false or not, if false then testcase will pass else fail

# assertIsNone: verifies weather iven value or expression result is None or Not, if none then pass else fail

# assertIsNotNone: opposite of assertIsNone

# assertIn: verifies weather the first element present in second element or not, if yes the pass else fail

# assertNotIn: opposite of assertIn
class TestAssertions(unittest.TestCase):

    # def test_asset_equal(self):
    #     driver = webdriver.Chrome()
    #     driver.get("https://www.google.co.in/")
    #     title = driver.title
    #
    #     # assertEqual
    #     self.assertEqual(title, "Google", "webpage title is not same")
    #     print(title)
    #     driver.quit()
    #
    # def test_asset_not_equal(self):
    #     driver = webdriver.Chrome()
    #     driver.get("https://www.google.co.in/")
    #     title = driver.title
    #
    #     self.assertNotEqual(title, "Gooogle", "webpage title is same")
    #     driver.close()
    #
    # def test_assert_true(self):
    #     driver = webdriver.Chrome()
    #     driver.get("https://www.google.co.in/")
    #     title = driver.title
    #     self.assertTrue(title=="Google", "webpage title is same")
    #     print(title)
    #     driver.quit()
    #
    # def test_assert_false(self):
    #     driver = webdriver.Chrome()
    #     driver.get("https://www.google.co.in/")
    #     title = driver.title
    #     self.assertFalse(title=="Google", "webpage title is not same")
    #     driver.quit()
    #
    # def test_assert_is_none(self):
    #     driver = None
    #     self.assertIsNone(driver, "Driver dont have any value")
    #
    # def test_assert_is_not_none(self):
    #     driver = webdriver.Chrome()
    #     self.assertIsNotNone(driver, "Driver have some value")

    def test_asset_in_notIn(self):
        list = ["python", "selenium", "java"]

        self.assertIn("python", list, "python is not present in list")
        self.assertNotIn("c++", list, "cpp is present in list")

    def test_assertion_relation_comparision(self):
        # assertGreater: 1st value is greater than 2nd or not
        self.assertGreater(100, 10)

        # assertGreaterEqual: 1st parameter >= 2nd parameter or not
        self.assertGreaterEqual(100, 100)

        # assertLess: 1st < 2nd
        self.assertLess(100, 1000)

        # assertLessEqual: 1st <= 2nd
        self.assertLessEqual(100, 100)


if __name__ == '__main__':
    unittest.main()