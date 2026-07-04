class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = 0
        e = len(nums) - 1
        n = len(nums)

        while s <= e:
            m = (s + e) // 2

            left = float('-inf') if m == 0 else nums[m - 1]
            right = float('-inf') if m == n - 1 else nums[m + 1]

            if nums[m] > left and nums[m] > right:
                return m
            elif nums[m] < right:
                s = m + 1
            else:
                e = m - 1