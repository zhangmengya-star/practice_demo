'''
152. 乘积最大子数组
给你一个整数数组 nums ，请你找出数组中乘积最大的连续子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。

示例 1:
输入: [2,3,-2,4]
输出: 6
解释: 子数组 [2,3] 有最大乘积 6。

示例 2:
输入: [-2,0,-1]
输出: 0
解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。
'''


class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        if length == 0:
            return 0

        min_product = min(nums)
        min_result = [min_product for i in range(length)]
        max_result = [min_product for i in range(length)]

        for i in range(length):
            if i == 0:
                min_result[i] = nums[i]
                max_result[i] = nums[i]
            else:
                min_result[i] = min(min_result[i - 1] * nums[i], max_result[i - 1] * nums[i], nums[i])
                max_result[i] = max(min_result[i - 1] * nums[i], max_result[i - 1] * nums[i], nums[i])

        return max(max_result)


if __name__ == '__main__':
    solution = Solution()
    nums = [-2]
    result = solution.maxProduct(nums)
    print(result)
