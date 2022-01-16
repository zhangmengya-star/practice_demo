class Solution(object):
    def rob(self, nums):
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
                max_count[i] = max(nums[i],nums[i-1])
            else:
                max_count[i] = max(max_count[i-2]+nums[i], max_count[i-1])
        return max_count[-1]

if __name__ == '__main__':
    solution = Solution()
    nums = [5,2,3,10]
    result = solution.rob(nums)
    print(result)