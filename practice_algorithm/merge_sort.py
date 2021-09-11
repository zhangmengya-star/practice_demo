''' 归并排序'''
'''
归并排序是建立在归并操作上的一种有效的排序算法。该算法是采用分治法（Divide and Conquer）的一个非常典型的应用。将已有序的子序列合并，得到完全有序的序列；即先使每个子序列有序，再使子序列段间有序。若将两个有序表合并成一个有序表，称为2-路归并。

算法描述

把长度为n的输入序列分成两个长度为n/2的子序列；
对这两个子序列分别采用归并排序；
将两个排序好的子序列合并成一个最终的排序序列。
'''


def merge(left, right):
    left_length = len(left)
    right_length = len(right)
    i = 0
    j = 0
    result = []
    while i < left_length and j < right_length:
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    if i < left_length:
        result.extend(left[i:left_length])
    if j < right_length:
        result.extend(left[j:right_length])
    return result


def merge_sort(list):
    length = len(list)
    if length <= 1:
        return list
    middle = int(length / 2)
    left = list[0:middle]
    right = list[middle:length]
    return merge(merge_sort(left), merge_sort(right))


if __name__ == '__main__':
    result = merge_sort([4, 3, 2, 1])
    print(result)
