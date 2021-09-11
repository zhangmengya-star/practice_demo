import pytest


@pytest.mark.login
def test_login_1():
    print("test_login_1")


@pytest.mark.login
def test_login_2():
    print("test_login_2")


@pytest.mark.login
def test_login_3():
    print("test_login_3")


@pytest.mark.search
def test_search_1():
    print("test_search_1")


@pytest.mark.search
def test_search_2():
    print("test_search_2")


@pytest.mark.search
def test_search_3():
    print("test_search_3")
