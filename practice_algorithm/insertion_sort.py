'''插入排序'''
'''
插入排序（Insertion-Sort）的算法描述是一种简单直观的排序算法。它的工作原理是通过构建有序序列，对于未排序数据，在已排序序列中从后向前扫描，找到相应位置并插入。

算法描述

一般来说，插入排序都采用in-place在数组上实现。具体算法描述如下：

从第一个元素开始，该元素可以认为已经被排序；
取出下一个元素，在已经排序的元素序列中从后向前扫描；
如果该元素（已排序）大于新元素，将该元素移到下一位置；
重复步骤3，直到找到已排序的元素小于或者等于新元素的位置；
将新元素插入到该位置后；
重复步骤2~5。
'''


def insertion_element(sorted_list: list, num):
    length = len(sorted_list)
    if length == 0:
        return [num]
    is_inserted = False
    for i in range(length):
        if sorted_list[i] > num:
            sorted_list.insert(i, num)
            is_inserted = True
            break
    if is_inserted is False:
        sorted_list.append(num)
    return sorted_list


def insertion_sort(list):
    length = len(list)
    if length <= 1:
        return length

    result_list = []
    for i in range(length):
        num = list[i]
        result_list = insertion_element(result_list, num)
    return result_list


if __name__ == '__main__':
    result = insertion_sort([6, 5, 4, 3, 1])
    print(result)
