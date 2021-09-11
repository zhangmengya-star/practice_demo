'''希尔排序'''
'''
希尔排序(Shell Sort)是插入排序的一种。也称缩小增量排序，是直接插入排序算法的一种更高效的改进版本。 希尔排序是把记录按下标的一定增量分组，对每组使用直接插入排序算法排序；随着增量逐渐减少，每组包含的关键词越来越多，当增量减至1时，整个文件恰被分成一组，算法便终止。

希尔排序的基本思想是：将数组列在一个表中并对列分别进行插入排序，重复这过程，不过每次用更长的列（步长更长了，列数更少了）来进行。最后整个表就只有一列了。将数组转换至表是为了更好地理解这算法，算法本身还是使用数组进行排序。
'''


def shell_sort(list):
    length = len(list)
    gap = int(length / 2)
    while gap > 0:
        for i in range(gap, length):
            j = i
            while j >= gap and list[j - gap] > list[j]:
                list[j - gap], list[j] = list[j], list[j - gap]
                j -= gap
        gap = int(gap / 2)
    return list


if __name__ == '__main__':
    result = shell_sort([1, 2, 3, 1, 2, 3])
    print(result)
