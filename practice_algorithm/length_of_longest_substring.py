'''
给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度。

示例 1:
输入: s = "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。

示例 2:
输入: s = "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。

示例 3:
输入: s = "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。

示例 4:
输入: s = ""
输出: 0
 

提示：

0 <= s.length <= 5 * 104
s 由英文字母、数字、符号和空格组成

链接：https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/
可以用滑动窗口？？
'''



class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s)
        result = []
        if length == 0:
            return 0
        for i in range(length):
            j = 0
            sub_str = s[i + j]
            while i + j + 1 < length:
                char = s[i + j + 1]
                if char in sub_str:
                    break
                else:
                    sub_str += char
                j += 1
            result.append(sub_str)
        num = len(result[0])
        for i in range(len(result)):
            if len(result[i]) > num:
                num = len(result[i])

        return num


if __name__ == '__main__':
    solution = Solution()
    s = 'pwwkew'
    print(solution.lengthOfLongestSubstring(s))

