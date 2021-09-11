import pytest


def test_function_1():
    print('test_function_1')


def test_function_2():
    print('test_function_2')


class TestClass:
    def test_method_1(self):
        print('test_method_1')
        assert 1 == 1

    @pytest.mark.custom
    def test_method_2(self):
        print('test_method_2')
        assert 2 == 3
        assert 3 == 4

    def test_method_3(self):
        print('test_method_3')
        pytest.assume(3 == 4)
        pytest.assume(4 == 5)
