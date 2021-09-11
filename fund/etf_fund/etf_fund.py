import requests
import time
from bs4 import BeautifulSoup
import xlwt

def search_fund(fund_key):
    ## 模拟在基金公司排名页，根据指数，查找对应的结果
    url = "http://fundsuggest.eastmoney.com/FundSearch/api/FundSearchPageAPI.ashx"

    time_stamp = get_now_timestamp()
    params = {}
    params['callback'] = f"jQuery18307043347253407186_{time_stamp}"
    params['key'] = fund_key
    params['m'] = 0
    params['_'] = time_stamp

    result = requests.get(url=url, params=params)
    data = result.text
    fund_list_total_count = data.split('"FundListTotalCount":')[1].split(',')[0]
    fund_list_total_count = int(fund_list_total_count)


    url = 'http://fundsuggest.eastmoney.com/FundSearch/api/FundSearchPageAPI.ashx'

    time_stamp = get_now_timestamp()
    params = {}
    params['callback'] = f"jQuery18307043347253407186_{time_stamp}"
    params['m'] = 1
    params['key'] = fund_key
    params['pageindex'] = 0
    params['pagesize'] = fund_list_total_count
    params['_'] = time_stamp
    result = requests.get(url=url, params=params)
    data = result.text
    data_1 = data.split('"Datas":[')[1].split(']')[0]
    data_2 = data_1.split('}')

    search_result = []

    for i in range(fund_list_total_count):
        fund_content = data_2[i].split(',')
        if i == 0:
            fund_code = fund_content[1].split('"CODE":')[1]
            fund_name = fund_content[2].split('"NAME":')[1]
        else:
            fund_code = fund_content[2].split('"CODE":')[1]
            fund_name = fund_content[3].split('"NAME":')[1]
        fund_code = fund_code.split('"')[1]
        fund_name = fund_name.split('"')[1]
        search_result.append({'fund_code': fund_code, 'fund_name': fund_name})
    return search_result


def get_now_timestamp():
    t = time.time()
    return int(round(t * 1000))


def fund_detail(fund_code, fund_name):
    '''
    :param fund_code: 基金编码
    :return: 基金详情，只返回需要的几个字段
    '''
    # 最后返回的结果
    fund_result = {
        'code': fund_code,
        'name': fund_name,
        'type': '',
        'scale': '',
        'date': '',
        'company': '',
        'company_scale': '',
        'tracking_index': '',
        'error_rate': '',
        'service_fee': '',
        'custody_fee': ''
    }

    url = f"http://fund.eastmoney.com/{fund_code}.html"
    result = requests.get(url)
    result.encoding = 'utf-8'
    result_text = result.text

    soup = BeautifulSoup(result_text, features="html.parser")

    # # 获取基金名称
    # fund_title_element = soup.find_all(class_='fundDetail-tit')[0]
    # fund_title_text = fund_title_element.get_text()
    # fund_result['name'] = fund_title_text.replace("\xa0", " ")


    # 获取基金详情
    fund_class_element = soup.find_all(class_='infoOfFund')
    if len(fund_class_element) > 0:
        # 可以找到对应元素
        info = fund_class_element[0].find_all('td')
        for i in info:
            text = i.get_text()
            if '基金类型' in text:
                temp = text.split('基金类型：')[1].split('|')[0]
                fund_result['type'] = temp.strip()
            if '基金规模' in text:
                temp = text.split('基金规模：')[1].split('（')[0]
                fund_result['scale'] = temp.strip()
            if '成 立 日' in text:
                temp = text.split('成 立 日：')[1]
                fund_result['date'] = temp.strip()
            if '管 理 人' in text:
                temp = text.split('管 理 人：')[1]
                fund_result['company'] = temp.strip()

                # 获取基金规模
                company_url = i.find_all('a')[0]['href']
                fund_result['company_scale'] = company_scale(company_url)
            if '跟踪标的：' in text:
                temp = text.split('|')
                temp_1 = temp[0].split('跟踪标的：')[1]
                temp_2 = temp[1].split('跟踪误差：')[1]
                fund_result['tracking_index'] = temp_1.strip()
                fund_result['error_rate'] = temp_2.strip()
        # 获取基金费率
        rate = fund_rate(fund_code)
        fund_result['service_fee'] = rate['service_fee']
        fund_result['custody_fee'] = rate['custody_fee']
    else:
        # 处理发生过一次重定向的问题，比如基金100032、100033就有这个问题
        location_href = result_text.split('location.href = ')[1].split(';')[0]
        code = location_href.split('/')[-1].split('.')[0]
        fund_result = fund_detail(code, fund_name)
    return fund_result


def fund_list(fund_key):
    result = []
    funds = search_fund(fund_key)
    for i in funds:
        print(i)
        code = i['fund_code']
        name = i['fund_name']
        detail = fund_detail(code, name)
        result.append(detail)
    return result


def company_scale(company_url):
    # 获取基金规模
    scale = ''
    result = requests.get(company_url)
    result.encoding = 'utf-8'
    result_text = result.text

    soup = BeautifulSoup(result_text, features="html.parser")
    scale_class_element = soup.find_all(class_='padding-left-10')

    if len(scale_class_element) > 0:
        text = scale_class_element[0].get_text()
        scale = text.split(':')[1].strip()
    return scale

def fund_rate(fund_code):
    result = {
        'service_fee': '',
        'custody_fee': ''
    }
    url = f"http://fundf10.eastmoney.com/jbgk_{fund_code}.html"
    res = requests.get(url)
    res.encoding = 'utf-8'
    res_text = res.text

    soup = BeautifulSoup(res_text, features="html.parser")
    class_element = soup.find_all(class_='info')[0]

    if len(class_element) > 0:
        ths = class_element.find_all('th')
        tds = class_element.find_all('td')
        for i in range(len(ths)):
            if ths[i].get_text() == '管理费率':
                result['service_fee'] = tds[i].get_text()
            if ths[i].get_text() == '托管费率':
                result['custody_fee'] = tds[i].get_text()
    return result



def write_excel(name, data):
    workbook = xlwt.Workbook()
    worksheet = workbook.add_sheet('etf_fund')

    head = ['代码', '基金名称', '类型', '规模', '成立日',
            '基金公司', '基金规模', '跟踪标的', '跟踪误差',
            '管理费率', '托管费率'
            ]

    # i 表示第几行，j表示第几列
    i = 0
    j = 0
    for title in head:
        worksheet.write(i, j, title)
        j += 1
    i += 1

    for fund in data:
        j = 0
        worksheet.write(i, j, fund['code'])
        j += 1
        worksheet.write(i, j, fund['name'])
        j += 1
        worksheet.write(i, j, fund['type'])
        j += 1
        worksheet.write(i, j, fund['scale'])
        j += 1
        worksheet.write(i, j, fund['date'])
        j += 1
        worksheet.write(i, j, fund['company'])
        j += 1
        worksheet.write(i, j, fund['company_scale'])
        j += 1
        worksheet.write(i, j, fund['tracking_index'])
        j += 1
        worksheet.write(i, j, fund['error_rate'])
        j += 1
        worksheet.write(i, j, fund['service_fee'])
        j += 1
        worksheet.write(i, j, fund['custody_fee'])
        i += 1

    workbook.save(f"{name}_fund.xls")


if __name__ == '__main__':
    key = '医药'
    funds = fund_list(key)

    write_excel(key, funds)

