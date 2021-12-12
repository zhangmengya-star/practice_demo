'''
704. 二分查找
给定一个 n 个元素有序的（升序）整型数组 nums 和一个目标值 target  ，写一个函数搜索 nums 中的 target，如果目标值存在返回下标，否则返回 -1。


示例 1:

输入: nums = [-1,0,3,5,9,12], target = 9
输出: 4
解释: 9 出现在 nums 中并且下标为 4
示例 2:

输入: nums = [-1,0,3,5,9,12], target = 2
输出: -1
解释: 2 不存在 nums 中因此返回 -1


提示：

你可以假设 nums 中的所有元素是不重复的。
n 将在 [1, 10000]之间。
nums 的每个元素都将在 [-9999, 9999]之间。

'''


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start = 0
        end = len(nums) - 1
        while start <= end:
            middle = int((start + end) / 2)
            if target < nums[middle]:
                end = middle - 1
            elif target == nums[middle]:
                return middle
            else:
                start = middle + 1
        return -1


if __name__ == '__main__':
    solution = Solution()
    nums = [-1, 0, 3, 5, 9, 12]
    target = 2
    result = solution.search(nums, target)
    print(result)

'''
测试用例：
target小于nums的最小值
target等于nums的最小值
target大于nums的最大值
target等于nums的最大值
target存在于nums中
target不存在于nums中
nums中的元素有重复
nums中元素的值过大
target的值过大
nums中的元素过多
'''
