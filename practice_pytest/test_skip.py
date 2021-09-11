import pytest
import sys


# 跳过测试用例
@pytest.mark.skip("此次测试不执行该条用例")
def test_skip():
    print("这条测试用例被跳过了")


# 在满足条件时，跳过测试用例
@pytest.mark.skipif(sys.platform == 'darwin', reason="不在macOs上执行")
def test_skip_if():
    print('该条测试用例有条件的被跳过')
