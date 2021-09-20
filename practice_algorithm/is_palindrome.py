'''
给你一个整数 x ，如果 x 是一个回文整数，返回 true ；否则，返回 false 。

回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。例如，121 是回文，而 123 不是。

 

示例 1：

输入：x = 121
输出：true
示例 2：

输入：x = -121
输出：false
解释：从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
示例 3：

输入：x = 10
输出：false
解释：从右向左读, 为 01 。因此它不是一个回文数。
示例 4：

输入：x = -101
输出：false
'''


# 解法一：将整数转换成字符串，进行字符串反转，反转后的结果与原来的字符串做对比
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        str_x = str(x)
        reverse_x = str_x[::-1]
        int_reverse_x = int(reverse_x)
        if x == int_reverse_x:
            return True
        else:
            return False


# 解法二：比如 123321，第一位和最后一位进行对比，第二位和倒数第二位进行对比，以此类推
class Solution_1(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        str_x = str(x)
        len_x = len(str_x)

        for i in range(len_x):
            if i <= len_x - i - 1:
                if str_x[i] == str_x[len_x - i - 1]:
                    continue
                else:
                    return False
            else:
                return True
        return True


if __name__ == '__main__':
    solution = Solution_1()
    result = solution.isPalindrome(10101)
    print(result)
