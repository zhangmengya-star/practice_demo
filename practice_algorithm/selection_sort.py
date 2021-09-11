'''选择排序'''
'''
选择排序(Selection-sort)是一种简单直观的排序算法。它的工作原理：首先在未排序序列中找到最小（大）元素，存放到排序序列的起始位置，然后，再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。以此类推，直到所有元素均排序完毕。
'''


def selection_sort(list):
    length = len(list)
    if length <= 1:
        return list
    for i in range(length-1):
        min_index = i
        min_value = list[i]
        for j in range(i + 1, length):
            if list[j] < min_value:
                min_index = j
                min_value = list[j]
        list[i], list[min_index] = list[min_index], list[i]
    return list

if __name__ == '__main__':
    result = selection_sort([3,2,1,3,2,1])
    print(result)
