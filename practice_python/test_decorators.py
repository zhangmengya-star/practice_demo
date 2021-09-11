'''
装饰器
'''
from functools import wraps


def extend(func):
    # wraps解决重写函数名字和注释文档的问题
    @wraps(func)
    def hello(*args, **kwargs):
        print('hello')
        func(*args, **kwargs)
        print('bye')

    return hello


# 带参数的装饰器
def extend_param(name):
    def extend(func):
        def hello(*args, **kwargs):
            print('hello')
            print(f'my name is {name}')
            func(*args, **kwargs)
            print('bye')

        return hello

    return extend


def function():
    print('function')


@extend
def function_1():
    print('function_1')


@extend_param('xiaoming')
def function_2():
    print('function_2')


def test_wrapper():
    # extend(function)() 相当于使用装饰器@extend的function()
    extend(function)()
    function_1()

    # 下面两句等同
    function_2()
    extend_param('xiaoming')(function)()




