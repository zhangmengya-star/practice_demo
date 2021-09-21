'''快速排序'''
'''
快速排序使用分治法（Divide and conquer）策略来把一个序列（list）分为较小和较大的2个子序列，然后递归地排序两个子序列。

步骤为：

挑选基准值：从数列中挑出一个元素，称为"基准"（pivot）;
分割：重新排序数列，所有比基准值小的元素摆放在基准前面，所有比基准值大的元素摆在基准后面（与基准值相等的数可以到任何一边）。在这个分割结束之后，对基准值的排序就已经完成;
递归排序子序列：递归地将小于基准值元素的子序列和大于基准值元素的子序列排序。
'''


def quick_sort(list):
    length = len(list)
    if length <= 1:
        return list
    left_list = []
    right_list = []
    standard = list[0]
    for i in range(1, length):
        if list[i] >= standard:
            right_list.append(list[i])
        else:
            left_list.append(list[i])
    left_list = quick_sort(left_list)
    right_list = quick_sort(right_list)
    result = []
    result.extend(left_list)
    result.append(standard)
    result.extend(right_list)
    return result


if __name__ == '__main__':
    list = [6, 6, 5, 4, 3, 2, 1]
    result = quick_sort(list)
    print(result)
