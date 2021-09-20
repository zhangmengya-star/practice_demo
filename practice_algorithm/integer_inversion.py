'''
给你一个 32 位的有符号整数 x ，返回将 x 中的数字部分反转后的结果。

如果反转后整数超过 32 位的有符号整数的范围 [−231,  231 − 1] ，就返回 0。

假设环境不允许存储 64 位整数（有符号或无符号）。
 

示例 1：

输入：x = 123
输出：321
示例 2：

输入：x = -123
输出：-321
示例 3：

输入：x = 120
输出：21
示例 4：

输入：x = 0
输出：0
 

提示：

-231 <= x <= 231 - 1
'''


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x >= 0:
            less_zero = False
        else:
            less_zero = True
        x_abs = abs(x)

        str_x = str(x_abs)
        str_x = str_x[::-1]

        if less_zero is True:
            result = int('-' + str_x)
        else:
            result = int(str_x)

        if abs(result) > 2 ** 31 - 1:
            return 0
        else:
            return result


class Solution_1(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        if x >= 0:
            less_zero = False
        else:
            less_zero = True

        x_abs = abs(x)
        result_abs = 0

        while True:
            num = x_abs % 10
            result_abs += num
            x_abs = int(x_abs / 10)
            if x_abs <= 0:
                break
            result_abs = result_abs * 10

        if abs(result_abs) > 2 ** 31 - 1:
            return 0

        if less_zero is True:
            return 0 - result_abs
        else:
            return result_abs


if __name__ == '__main__':
    solution = Solution_1()
    result = solution.reverse(1563847412)
    print(result)
