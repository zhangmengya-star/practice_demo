# coding=utf-8
import sys
'''
题目：找出2个数组中相同的元素，且它们的索引和最小
输入:
["A", "B", "C", "D"]
["E", "F", "G", "A"]
输出: ["A"]

输入:
["A", "B", "C", "D"]
["E", "F", "B", "A"]
输出: ["A","B"]
'''

def function(list_1, list_2):
    list_1_len = len(list_1)
    list_2_len = len(list_2)
    if list_1_len == 0 or list_2_len == 0:
        return None

    result = {}
    for key, value in enumerate(list_1):
        if value in result.keys():
            continue
        if value in list_2:
            index_2 = list_2.index(value)
            result[value] = key + index_2

    if len(result) == 0:
        return None

    count = 9999
    result_char = []
    for i in result.keys():
        if result[i] <= count:
            count = result[i]
            result_char.append(i)
    return result_char


list_1 = ["A", "B", "C", "D"]
list_2 = ["E", "F", "B", "A"]
result = function(list_1, list_2)
print(result)






