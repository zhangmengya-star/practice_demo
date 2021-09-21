'''
数字拼接
给出一个数组，如 [7864, 284, 347, 7732, 8498]，
现在需要将数组中的数字拼接起来，如按顺序依次拼接为：786428434777328498，数组中的数字拼接顺序可以任意，
编写程序，返回「最大的可能拼出的数字」。（以上面数组为例，返回：849878647732347284）
'''


def number_splicing(list: list):
    # list.sort(reverse=True)
    # length = len(list)
    # result = ''
    # for i in range(length):
    #     num_str = str(list[i])
    #     result = result + num_str
    # return result
    length = len(list)
    str_list = []
    for i in range(length):
        num_str = str(list[i])
        str_list.append(num_str)

    for i in range(length - 1):
        for j in range(length - i - 1):
            str_list[j], str_list[j + 1] = str_sort(str_list[j], str_list[j + 1])
    return str_list


def str_sort(str_1, str_2):
    result_1 = str_1 + str_2
    result_2 = str_2 + str_1
    if result_1 >= result_2:
        return str_1, str_2
    else:
        return str_2, str_1


if __name__ == '__main__':
    a = number_splicing([7864, 284, 347, 7732, 8498])
    print(a)
