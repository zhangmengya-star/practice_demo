import pytest


# 解决自定义标签有警告的问题
def pytest_configure(config):
    markers_list = ["custom", "search", "login"]
    for markers in markers_list:
        config.addinivalue_line(
            "markers", markers
        )


@pytest.fixture(scope="function")
def login():
    print("登录操作，部分测试用例需要登录")

# @pytest.fixture(autouse=True)
# def open_browser():
#     print("每个测试用例都需要执行")
