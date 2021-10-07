'''冒泡排序'''
'''预期结果：列表从小到大排序'''


def bubble_sort(list):
    length = len(list)
    if length <= 1:
        return list

    for i in range(length - 1):
        for j in range(length - 1 - i):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]

    return list


if __name__ == '__main__':
    list_1 = [5, 4, 3, 2, 1]
    list_1 = bubble_sort(list_1)
    print(list_1)

    list_2 = [1]
    list_2 = bubble_sort(list_2)
    print(list_2)

    list_3 = []
    list_3 = bubble_sort(list_3)
    print(list_3)
