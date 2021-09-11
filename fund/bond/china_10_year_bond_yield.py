'''
中国十年期国债收益率
当前10年期国债收益率>3.27%，买入债券基金；
当前10年期国债收益率<3%，卖出债券基金。
'''

import requests
from bs4 import BeautifulSoup

def get_bond_yield():
    url = 'https://cn.investing.com/rates-bonds/china-10-year-bond-yield'
    header = {}
    header['Host'] = 'cn.investing.com'
    header['Connection'] = 'keep-alive'
    header['Pragma'] = 'no-cache'
    header['Cache-Control'] = 'no-cache'
    header['Upgrade-Insecure-Requests'] = '1'
    header['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'
    header['Accept'] = 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
    header['Sec-Fetch-Site'] = 'none'
    header['Sec-Fetch-Mode'] = 'navigate'
    header['Sec-Fetch-Dest'] = 'document'
    header['Accept-Encoding'] = 'gzip, deflate, br'
    header['Accept-Language'] = 'zh-CN,zh;q=0.9'
    res = requests.get(url=url, headers=header)

    if res.status_code != 200:
        print(res.text)
        raise Exception('接口响应报错了')

    res_text = res.text
    soup = BeautifulSoup(res_text, features="html.parser")
    elements = soup.find_all(id="last_last")

    if len(elements) <= 0:
        raise Exception('页面上没有找到数据')

    bond_yield = elements[0].text
    return bond_yield


def judge_timing():
    bond_yield = get_bond_yield()
    print(f"当前中国十年期国债收益率为:{bond_yield}")

    if float(bond_yield) > 3.27:
        print('大于3.27%,现在是买入债券的时机啦')
    elif float(bond_yield) < 3:
        print('小于3%,现在是卖出债券的时机啦')
    else:
        print('不满足条件，继续观望')


if __name__ == '__main__':
    judge_timing()
