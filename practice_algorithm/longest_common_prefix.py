'''
14. 最长公共前缀
编写一个函数来查找字符串数组中的最长公共前缀。
如果不存在公共前缀，返回空字符串 ""。


示例 1：

输入：strs = ["flower","flow","flight"]
输出："fl"
示例 2：

输入：strs = ["dog","racecar","car"]
输出：""
解释：输入不存在公共前缀。


提示：

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] 仅由小写英文字母组成
'''


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        strs_length = len(strs)
        if strs_length == 0:
            return ''
        elif strs_length == 1:
            return strs[0]

        strand = strs[0]
        result = ''
        for index, value in enumerate(strand):
            is_exist = True
            for str in strs:
                if len(str) < index + 1:
                    is_exist = False
                    break
                if str[index] != value:
                    is_exist = False
                    break
            if is_exist is True:
                result += value
            else:
                break
        return result


if __name__ == '__main__':
    solution = Solution()
    strs = ["flower", "flow", "flight"]
    result = solution.longestCommonPrefix(strs)
    print(result)

    strs = ["flower", "fq"]
    result = solution.longestCommonPrefix(strs)
    print(result)

'''
测试用例：
列表为空
列表长度为1
列表长度为199
列表长度为200
列表中存在某个字符串长度为0
列表中存在某个字符串长度为1
列表中存在某个字符串长度为199
列表中存在某个字符串长度为200
列表中存在某个字符串包含除小写字母外的其他字符
不存在公共前缀
公共前缀只有1位
公共前缀有多位
列表中所有字符串内容相同
列表中的字符串长度不一致
列表中字符串的第一位相同，第二位不同，第三位相同：公共前缀只有第一位
列表中字符串的第一位不同，第二位相同：无公共前缀
列表中的字符串的第一位相同，第二位部分相同：公共前缀只有第一位
'''
