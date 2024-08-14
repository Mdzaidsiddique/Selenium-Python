import pytest

#want to execute setup this method before every test methods,need to  decorate and pass in methods parameter
@pytest.fixture
def setup():
    print("Once before every method")
# this setup is now fixture not method anymore

def test_method1(setup):
    print("this is test method 1 fx")

def test_method2(setup):
    print("this is test method 2 fx")