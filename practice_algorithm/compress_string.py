'''
字符串压缩。利用字符重复出现的次数，编写一种方法，实现基本的字符串压缩功能。比如，字符串aabcccccaaa会变为a2b1c5a3。若“压缩”后的字符串没有变短，则返回原先的字符串。你可以假设字符串中只包含大小写英文字母（a至z）。

示例1:
输入："aabcccccaaa"
输出："a2b1c5a3"

示例2:
输入："abbccd"
输出："abbccd"
解释："abbccd"压缩后为"a1b2c2d1"，比原字符串长度更长。
'''

class Solution(object):
    def compressString(self, S):
        """
        :type S: str
        :rtype: str
        """
        length = len(S)
        if length == 0:
            return S
        ch = S[0]
        ch_num = 0
        result = ''
        for i in S:
            if i == ch:
                ch_num += 1
            else:
                result += ch
                result += str(ch_num)
                ch = i
                ch_num = 1
        result += ch
        result += str(ch_num)
        if len(result) >= length:
            return S
        else:
            return result

if __name__ == '__main__':
    solution = Solution()
    result = solution.compressString('abbccd')
    print(result)


