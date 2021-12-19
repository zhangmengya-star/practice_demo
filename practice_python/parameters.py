'''包裹参数'''


def f(*a, **b):
    print(a)
    print(b)


a = 3
b = 4
f(a, b, m=1, n=2)


def f(*a, **b):
    print(a)
    print(b)


'''解包裹'''


def unpackage(a, b, c):
    print(a, b, c)


args = (1, 3, 4)
unpackage(*args)

args = {"a": 1, "b": 2, "c": 3}
unpackage(**args)
