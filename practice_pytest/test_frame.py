# 文档链接：https://docs.pytest.org/en/stable/xunit_setup.html?highlight=setup_class


def setup_module():
    print('setup_module')


def teardown_module():
    print('teardown_module')


def setup_function():
    print('setup_function')


def teardown_function():
    print('teardown_function')


def test_function_1():
    print('test_function_1')


def test_function_2():
    print('test_function_2')


class TestClass:
    @classmethod
    def setup_class(self):
        print('setup_class')

    @classmethod
    def teardown_class(self):
        print('teardown_class')

    def setup_method(self):
        print('setup_method')

    def teardown_method(self):
        print('teardown_method')

    def setup(self):
        print('setup')

    def teardown(self):
        print('teardown')

    def test_method_1(self):
        print('test_method_1')

    def test_method_2(self):
        print('test_method_2')
