'''
大数相加
'''
'''
解题思路：
1.进行长度补零，即让两个要计算的字符串长度一样。
2.将两个字符串，分解成列表，并进行翻转(翻转后，个位在前，目的，从个位往高位计算)
3.创建一个长度与要计算的字符串长度相同的列表，元素填充为0.
4.遍历列表，由于两个列表长度相同，遍历任何一个都可以。
5.由于是10进制，所以两个值累加后与10进行比较，大于等于即有进位。
'''


def large_number_addition(num_1: str, num_2: str):
    len_number_1 = len(num_1)
    len_number_2 = len(num_2)

    # 进行长度补0
    if len_number_1 > len_number_2:
        str_len = len_number_1
        num_2 = num_2.rjust(str_len, '0')
    else:
        str_len = len_number_2
        num_1 = num_1.rjust(str_len, '0')

    # 将字符串分解成列表
    num_1 = list(num_1)
    num_2 = list(num_2)

    # 列表翻转
    # list_number_1 = sorted(num_1, reverse=True)
    # list_number_2 = sorted(num_2, reverse=True)
    list_number_1 = num_1[::-1]
    list_number_2 = num_2[::-1]
    # list_number_1 = list(reversed(num_1))
    # list_number_2 = list(reversed(num_2))

    # 进行计算
    result = []
    greater_ten = 0
    for i in range(str_len):
        sum = int(list_number_1[i]) + int(list_number_2[i])

        if sum + greater_ten >= 10:
            result.append(str(sum + greater_ten - 10))
            greater_ten = 1
        else:
            result.append(str(sum + greater_ten))
            greater_ten = 0

    # reversed_list = list(reversed(result))
    reversed_list = result[::-1]
    # reversed_list = sorted(result, reverse=True)

    return "".join(reversed_list)


if __name__ == '__main__':
    a = '12345'
    b = '55'
    c = large_number_addition(a, b)
    print(c)
