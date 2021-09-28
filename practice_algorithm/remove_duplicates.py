'''
删除有序数组中的重复项

给你一个有序数组 nums ，请你 原地 删除重复出现的元素，使每个元素 只出现一次 ，返回删除后数组的新长度。

不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。
'''


class Solution(object):
    def removeDuplicates_bak(self, nums: list):
        # 不满足空间复杂度的要求
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)

        if length == 0 or length == 1:
            return length

        need = True

        while need is True:
            i = 0
            while i <= length - 2:
                if nums[i] == nums[i + 1]:
                    nums.remove(nums[i])
                    break
                if i == length - 2:
                    need = False
                i += 1
            length = len(nums)

        return length

    def removeDuplicates(self, nums: list):
        # 双指针
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)

        if length == 0:
            return length

        slow = 1
        fast = 1
        while fast <= length - 1:
            if nums[fast] != nums[fast - 1]:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1

        return slow


if __name__ == '__main__':
    solution = Solution()
    nums = [1, 1, 2, 2, 2, 3, 3, 4, 4, 5]
    solution.removeDuplicates(nums)
    print(nums)

    nums_1 = [1, 2, 3, 4, 5]
    solution.removeDuplicates(nums_1)
    print(nums_1)
