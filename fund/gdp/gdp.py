import requests
import json
import ast



url = 'http://datainterface.eastmoney.com/EM_DataCenter/JS.aspx'
param = {}
param['cb'] = 'datatable8201751'
param['type'] = 'GJZB'
param['sty'] = 'ZGZB'
param['js'] = '({data:[(x)],pages:(pc)})'
param['p'] = 1
param['ps'] = 20
param['mkt'] = 20
res = requests.get(url=url, params=param)
if res.status_code != 200:
    print('接口报错了')
# res_data = res.text.split('{')[1].split('}')[0]
# data_1 = res_data.split('pages:')
# pages = data_1[1]
# data_2 = data_1[0].split('data:[')[1].split('],')[0]
# data_3 = data_2.split('","')
# for data_4 in data_3:
#     data_5 = data_4.split(',')
#     data_6 = data_5[0]
#     if data_6[-5:] == '12-01':
#         print(data_6[-10:])
#         print(data_5[2])
text = res.text.split('(')[1].split(')')[0]
print(text)
# print(json.loads(text))
#print(eval(text))


