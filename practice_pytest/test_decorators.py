def my_fixture(func):
    def setup_teardown():
        print('start')
        func()
        print('end')

    return setup_teardown


@my_fixture
def testcase():
    print('test case')


testcase()
