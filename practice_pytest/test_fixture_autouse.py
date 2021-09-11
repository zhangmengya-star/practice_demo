import pytest


@pytest.fixture(autouse=True)
def login():
    print('login')


def test_one():
    print('one')
    assert 1 == 1


def test_two():
    print('two')
    assert 2 == 2


def test_three():
    print('three')
    assert 3 == 3