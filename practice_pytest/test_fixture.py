import pytest


@pytest.fixture()
def login():
    print('login')


def test_one(login):
    print('one')
    assert 1 == 1


def test_two():
    print('two')
    assert 2 == 2


def test_three(login):
    print('three')
    assert 3 == 3
