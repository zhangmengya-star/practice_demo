import pytest


@pytest.mark.xfail
def test_fail():
    print('test_fail')
    raise Exception


@pytest.mark.xfail
def test_pass():
    print('test_pass')
