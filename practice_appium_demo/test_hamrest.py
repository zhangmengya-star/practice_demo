from hamcrest import *


class TestHamrest:
    def test_hamrest_1(self):
        assert_that(10, equal_to(10), '这是一个提示')
        print('test_hamrest_1')

    def test_hamrest_2(self):
        assert_that(12, close_to(10, 2))
        print('test_hamrest_2')

    def test_hamrest_3(self):
        assert_that('hello world', contains_string('hello'))
        print('test_hamrest_3')

    def test_hamrest_4(self):
        # 第一个断言执行失败后，不会再执行后面的断言
        assert_that(9, equal_to(10), '这是一个提示')
        assert_that(9, close_to(10.0, 2.0))
        print('test_hamrest_4')
