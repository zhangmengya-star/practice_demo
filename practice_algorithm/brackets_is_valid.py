'''
20. 有效的括号
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。


示例 1：

输入：s = "()"
输出：true
示例 2：

输入：s = "()[]{}"
输出：true
示例 3：

输入：s = "(]"
输出：false
示例 4：

输入：s = "([)]"
输出：false
示例 5：

输入：s = "{[]}"
输出：true


提示：

1 <= s.length <= 10^4
s 仅由括号 '()[]{}' 组成
'''


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s_length = len(s)
        if s_length % 2 == 1:
            return False
        stack = []
        is_valid = True
        for i in range(s_length):
            if s[i] == '(' or s[i] == '[' or s[i] == '{':
                stack.append(s[i])
            if s[i] == ')':
                if len(stack) > 0 and stack[-1] == '(':
                    stack.pop()
                else:
                    is_valid = False
                    break
            if s[i] == ']':
                if len(stack) > 0 and stack[-1] == '[':
                    stack.pop()
                else:
                    is_valid = False
                    break
            if s[i] == '}':
                if len(stack) > 0 and stack[-1] == '{':
                    stack.pop()
                else:
                    is_valid = False
                    break

        if is_valid == False or len(stack) > 0:
            return False
        else:
            return True


if __name__ == '__main__':
    solution = Solution()
    s = '{[]}'
    result = solution.isValid(s)
    print(result)

'''
测试用例：
长度为空
长度为1
长度为奇数
长度为偶数&都是左括号(三种左括号)
长度为偶数&都是右括号(三种右括号)
长度为偶数&第一个字符为右括号
长度为偶数&排布为左右左右左右...(一种括号)
长度为偶数&排布为左右左右左右...(三种括号)可以匹配成功/不可以匹配成功
长度为偶数&排布为左左左右右右...(一种括号)
长度为偶数&排布为左左左右右右...(三种括号)可以匹配成功/不可以匹配成功
长度为偶数&左括号数大于右括号数
长度为偶数&左括号数小于右括号数
长度过长
包含除'()[]{}'的其他字符
'''
