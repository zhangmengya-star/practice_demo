import pytest


# yield 在第一次执行到yield时，只执行yield之前的内容
# 第二次执行到yield时，只执行yield之后到内容
@pytest.fixture(scope="module")
def login():
    print('login')

    yield

    print('clear')


def test_one():
    print('one')
    assert 1 == 1


def test_two(login):
    print('two')
    assert 2 == 2


def test_three(login):
    print('three')
    assert 3 == 3
