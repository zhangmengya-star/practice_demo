import pytest


@pytest.mark.parametrize("content, expected", [("3+5", 8), ("2+5", 7), ("7*5", 35)])
# 也可以写为 @pytest.mark.parametrize(["content", "expected"], [("3+5", 8), ("2+5", 7), ("7*5", 35)])
def test_eval(content, expected):
    print(f"content为{content},expected为{expected}")
    assert eval(content) == expected


@pytest.mark.parametrize("x", [1, 2])
@pytest.mark.parametrize("y", [3, 4])
def test_foo(x, y):
    print(f"x的值为{x},y的值为{y}")
    # 共输出4组数据，（1,3）（2,3）（1,4）（2,4）


test_user_data = ['xiaoming', 'xiaohong']


@pytest.fixture(scope="module")
def login_r(request):
    # 接收传入的参数
    user = request.param
    print(f"login_r登录的用户为{user}")
    return user


# indirect=True 可以把传过来的参数当函数执行
@pytest.mark.parametrize("login_r", test_user_data, indirect=True)
def test_login(login_r):
    a = login_r
    print(f"login登录的用户为{a}")
