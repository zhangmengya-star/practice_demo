'''
746. 使用最小花费爬楼梯
给你一个整数数组 cost ，其中 cost[i] 是从楼梯第 i 个台阶向上爬需要支付的费用。一旦你支付此费用，即可选择向上爬一个或者两个台阶。
你可以选择从下标为 0 或下标为 1 的台阶开始爬楼梯。
请你计算并返回达到楼梯顶部的最低花费。

示例 1：

输入：cost = [10,15,20]
输出：15
解释：你将从下标为 1 的台阶开始。
- 支付 15 ，向上爬两个台阶，到达楼梯顶部。
总花费为 15 。

示例 2：
输入：cost = [1,100,1,1,1,100,1,1,100,1]
输出：6
解释：你将从下标为 0 的台阶开始。
- 支付 1 ，向上爬两个台阶，到达下标为 2 的台阶。
- 支付 1 ，向上爬两个台阶，到达下标为 4 的台阶。
- 支付 1 ，向上爬两个台阶，到达下标为 6 的台阶。
- 支付 1 ，向上爬一个台阶，到达下标为 7 的台阶。
- 支付 1 ，向上爬两个台阶，到达下标为 9 的台阶。
- 支付 1 ，向上爬一个台阶，到达楼梯顶部。
总花费为 6 。

提示：
2 <= cost.length <= 1000
0 <= cost[i] <= 999

解题思路：
假设数组cost的长度为n，则n个阶梯分别对应下标0到n−1，楼层顶部对应下标n，问题等价于计算达到下标n的最小花费。可以通过动态规划求解。
创建长度为n+1的数组dp，其中dp[i]表示达到下标i的最小花费。
由于可以选择下标0或1作为初始阶梯，因此有dp[0]=dp[1]=0。
当2≤i≤n时，可以从下标i−1使用cost[i−1]的花费达到下标i，或者从下标i−2使用cost[i−2]的花费达到下标i。为了使总花费最小，dp[i]应取上述两项的最小值，因此状态转移方程如下：
dp[i]=min(dp[i−1]+cost[i−1],dp[i−2]+cost[i−2])

依次计算dp中的每一项的值，最终得到的dp[n] 即为达到楼层顶部的最小花费。
'''


class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        length = len(cost) + 1
        dp = [0 for i in range(length)]
        for i in range(length):
            if i == 0 or i == 1:
                dp[i] = 0
            else:
                dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])
        return dp[-1]


if __name__ == '__main__':
    solution = Solution()
    cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    result = solution.minCostClimbingStairs(cost)
    print(result)
