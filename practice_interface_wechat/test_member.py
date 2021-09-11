import pytest
import requests
from pip._vendor.lockfile import FileLock


def create_data():
    data = [(f"zhangsan{x}", f"zhangsan{x}", '189%08d' % x) for x in range(10)]
    return data


@pytest.fixture(scope='session')
def test_get_token():
    corpid = 'ww0605f79d546bc491'
    corpsecret = 'd4fYK3Br9v7f71JOeOsTa7tfVcCsas2XF3wPsm37SIU'
    url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken'
    params = {
        'corpid': corpid,
        'corpsecret': corpsecret
    }
    res = requests.get(url=url, params=params)
    return res.json()['access_token']


def test_add_member(userid, name, mobile, access_token):
    url = 'https://qyapi.weixin.qq.com/cgi-bin/user/create'
    params = {
        'access_token': access_token
    }
    payload = {
        "userid": userid,
        "name": name,
        "mobile": mobile,
        "department": [1]
    }
    res = requests.post(url=url, params=params, json=payload)
    return res.json()


def test_update_member(userid, name, mobile, access_token):
    url = 'https://qyapi.weixin.qq.com/cgi-bin/user/update'
    params = {
        'access_token': access_token
    }
    payload = {
        "userid": userid,
        "name": name,
        "mobile": mobile,
        "department": [1]
    }
    res = requests.post(url=url, params=params, json=payload)
    return res.json()


def test_delete_member(userid, access_token):
    url = 'https://qyapi.weixin.qq.com/cgi-bin/user/delete'
    params = {
        'access_token': access_token,
        'userid': userid
    }
    res = requests.get(url=url, params=params)
    return res.json()


def test_get_member(userid, access_token):
    url = 'https://qyapi.weixin.qq.com/cgi-bin/user/get'
    params = {
        'access_token': access_token,
        'userid': userid
    }
    res = requests.get(url=url, params=params)
    return res.json()


@pytest.mark.parametrize("userid, name, mobile", create_data())
def test_all(userid, name, mobile, test_get_token):
    add_result = test_add_member(userid, name, mobile, test_get_token)
    assert 0 == add_result['errcode']
    get_result = test_get_member(userid, test_get_token)
    assert 0 == get_result['errcode']
    assert userid == get_result['userid']
    assert name == get_result['name']

    update_name = name + '01'
    update_result = test_update_member(userid, update_name, mobile, test_get_token)
    assert 0 == update_result['errcode']
    get_result = test_get_member(userid, test_get_token)
    assert 0 == get_result['errcode']
    assert userid == get_result['userid']
    assert update_name == get_result['name']

    delete_result = test_delete_member(userid, test_get_token)
    assert 0 == delete_result['errcode']
    get_result = test_get_member(userid, test_get_token)
    assert 60111 == get_result['errcode']
