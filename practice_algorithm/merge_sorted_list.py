'''
合并两个有序数组

给你两个按 非递减顺序 排列的整数数组 nums1 和 nums2，另有两个整数 m 和 n ，分别表示 nums1 和 nums2 中的元素数目。
请你 合并 nums2 到 nums1 中，使合并后的数组同样按 非递减顺序 排列。
注意：最终，合并后数组不应由函数返回，而是存储在数组 nums1 中。为了应对这种情况，nums1 的初始长度为 m + n，其中前 m 个元素表示应合并的元素，后 n 个元素为 0 ，应忽略。nums2 的长度为 n 。
'''


class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """

        length = m + n
        index_length = length - 1
        index_m = m - 1
        index_n = n - 1
        while index_m >= 0 and index_n >= 0:
            if nums1[index_m] > nums2[index_n]:
                nums1[index_length] = nums1[index_m]
                index_m -= 1
            else:
                nums1[index_length] = nums2[index_n]
                index_n -= 1
            index_length -= 1
        if index_n >= 0:
            nums1[0:index_length + 1] = nums2[0:index_n + 1]


if __name__ == '__main__':
    nums1 = [4, 5, 6, 0, 0, 0]
    m = 3
    nums2 = [1, 2, 3]
    n = 3
    solution = Solution()
    solution.merge(nums1, m, nums2, n)
    print(nums1)

    nums1 = [0]
    m = 0
    nums2 = [6]
    n = 1
    solution = Solution()
    solution.merge(nums1, m, nums2, n)
    print(nums1)
