'''
在一个长为 字符串中找到第一个只出现一次的字符,并返回它的位置, 如果没有则返回 -1（需要区分大小写）.（从0开始计数）


数据范围：0 <= n <= 10000，且字符串只有字母组成。
要求：空间复杂度 O(n)，时间复杂度 O(n)

'''
import collections


class Solution(object):
    def firstUniqChar(self, s):
        # 借用s.count(str)计算字符出现的次数
        """
        :type s: str
        :rtype: str
        """
        length = len(s)

        if length == 0:
            return -1

        for i in range(length):
            if s.count(s[i]) == 1:
                return i
        return -1

    def firstUniqChar_1(self, s):
        frequency = collections.Counter(s)
        for i, ch in enumerate(s):
            if frequency[ch] == 1:
                return i
        return -1

    def firstUniqChar_2(self, s):
        length = len(s)
        if length == 0:
            return -1
        result = dict()

        for i in range(length):
            if s[i] in result.keys():
                result[s[i]] += 1
            else:
                result[s[i]] = 1

        for i in range(length):
            if result[s[i]] == 1:
                return i
        return -1


if __name__ == '__main__':
    solution = Solution()
    s = 'google'
    print(solution.firstUniqChar(s))
    print(solution.firstUniqChar_1(s))
    print(solution.firstUniqChar_2(s))
