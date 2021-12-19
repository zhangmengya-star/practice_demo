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

    def lengthOfLongestSubstring_1(self, s):
        length = len(s)
        if length <= 1:
            return length
        result = 1
        sub_str = s[0]
        i = 0
        j = 1
        while j < length:
            if s[j] in sub_str:
                while i < j:
                    if s[i] != s[j]:
                        i += 1
                    else:
                        i += 1
                        break
                sub_str = s[i:j + 1]
            else:
                sub_str += s[j]
            j += 1
            result = max(result, len(sub_str))

        return result


if __name__ == '__main__':
    solution = Solution()
    s = 'pwwkew'
    result = solution.lengthOfLongestSubstring_1(s)
    print(result)

'''
测试用例：
字符串长度为0
字符串长度为1
字符串长度为最大值-1
字符串长度为最大值
字符串长度为最大值+1
字符中包含除小写字母外的其他字符
字符串中的字符内容一致
字符串中的字符内容完全不一致
最长子串存在多个
最长子串的出现位置在字符串头部
最长子串的出现位置在字符串的中间某位置
最长子串的出现位置在字符串的尾部
最长子序列大于最长子串
'''
