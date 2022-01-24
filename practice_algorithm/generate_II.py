'''
119. 杨辉三角 II
给定一个非负索引 rowIndex，返回「杨辉三角」的第 rowIndex 行。
在「杨辉三角」中，每个数是它左上方和右上方的数的和。

示例 1:
输入: rowIndex = 3
输出: [1,3,3,1]

示例 2:
输入: rowIndex = 0
输出: [1]

示例 3:
输入: rowIndex = 1
输出: [1,1]
 
提示:
0 <= rowIndex <= 33

'''

import copy


class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        result = [0] * (rowIndex + 1)
        temp = [0] * (rowIndex + 1)

        for i in range(rowIndex + 1):
            j = 0
            while j <= i:
                if j == 0 or j == i:
                    result[j] = 1
                else:
                    result[j] = temp[j - 1] + temp[j]
                j += 1
            temp = copy.deepcopy(result)
        return result


if __name__ == '__main__':
    solution = Solution()
    result = solution.getRow(3)
    print(result)
