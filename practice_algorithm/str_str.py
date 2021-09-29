'''
实现 strStr()函数

给你两个字符串 haystack 和 needle ，请你在 haystack 字符串中找出 needle 字符串出现的第一个位置（下标从 0 开始）。如果不存在，则返回  -1 。


说明：

当 needle 是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。

对于本题而言，当 needle 是空字符串时我们应当返回 0 。这与 C 语言的 strstr() 以及 Java 的 indexOf() 定义相符。
'''


class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

        len_haystack = len(haystack)
        len_needle = len(needle)
        if len_needle == 0:
            return 0

        if len_needle > len_haystack or len_haystack == 0:
            return -1

        for i in range(len_haystack - len_needle + 1):
            if haystack[i:i + len_needle] == needle:
                return i
        return -1


if __name__ == '__main__':
    solution = Solution()
    haystack = 'abcdbc'
    needle = 'bc'
    result = solution.strStr(haystack, needle)
    print(result)
