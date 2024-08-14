# pytest is one of the unit testing framework which is implemented on the top of python unittest framework
# it contains lot of features when you compare with unittest
# pytest fw makes it easy to write small test

# installation
# pip install pytest
# pytest - -version

import pytest

def test_TestMethod1():
    print("This is test method 1")

def test_TestMethod2():
    print("This is test method 2")

# to run only type in terminal
# pytest
# pytest -v -s: (-v fpor some details, -s for print statements)
# pytest -v -s test_01_pytest_demo.py (module name), other wise it will execute all the module

# multiple ways to run test case in pytest


# pytest -v -s absolute path (run all test from module)
# pytest -v -s test_name.py::method_name (run sp test method from a module)
