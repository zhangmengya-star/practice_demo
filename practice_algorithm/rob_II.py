'''
213. 打家劫舍 II
你是一个专业的小偷，计划偷窃沿街的房屋，每间房内都藏有一定的现金。这个地方所有的房屋都 围成一圈 ，这意味着第一个房屋和最后一个房屋是紧挨着的。同时，相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警 。
给定一个代表每个房屋存放金额的非负整数数组，计算你 在不触动警报装置的情况下 ，今晚能够偷窃到的最高金额。

示例 1：
输入：nums = [2,3,2]
输出：3
解释：你不能先偷窃 1 号房屋（金额 = 2），然后偷窃 3 号房屋（金额 = 2）, 因为他们是相邻的。

示例 2：
输入：nums = [1,2,3,1]
输出：4
解释：你可以先偷窃 1 号房屋（金额 = 1），然后偷窃 3 号房屋（金额 = 3）。
     偷窃到的最高金额 = 1 + 3 = 4 。

示例 3：
输入：nums = [0]
输出：0


提示：
1 <= nums.length <= 100
0 <= nums[i] <= 1000
'''


class Solution(object):
    def rob_1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        if length == 0:
            return 0
        max_count = [0 for i in range(length)]
        for i in range(length):
            if i == 0:
                max_count[i] = nums[i]
            elif i == 1:
                max_count[i] = max(nums[i], nums[i - 1])
            else:
                max_count[i] = max(max_count[i - 2] + nums[i], max_count[i - 1])
        return max_count[-1]

    def rob(self, nums):
        length = len(nums)
        if length == 0:
            return 0
        elif length == 1:
            return nums[0]
        # 偷第一间房间，不能偷最后一间房：动态规划下标为[0,n-2]
        count_1 = self.rob_1(nums[0:length - 1:])
        # 偷最后一间房间，不能偷第一间房：动态规划下标为[1,n-1]
        count_2 = self.rob_1(nums[1:length:])
        return max(count_1, count_2)


if __name__ == '__main__':
    solution = Solution()
    nums = [1]
    result = solution.rob(nums)
    print(result)
