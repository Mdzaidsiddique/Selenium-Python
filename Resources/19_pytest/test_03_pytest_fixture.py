import pytest

@pytest.yield_fixture()
def setup():
    print("once before every method")
    yield #pause the execution , methods will execurte and after that below statement will execute
    print("once after every method")

def test_method11(setup):
    print("test_method11")

def test_method22(setup):
    print("test_method22")
