"""
Problem: Find Minimum in Rotated Sorted Array
Platform: LeetCode
Link: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
Approach: Binary Search
Time Complexity: O(log n)
Space Complexity: O(1)
"""

class Solution(object):

    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if not nums:
            return 0

        if len(nums) == 1:
            return nums[0]

        # Array already sorted
        if nums[0] < nums[len(nums) - 1]:
            return nums[0]

        Min = 0
        Max = len(nums) - 1

        while Min < Max:

            Mid = (Min + Max) // 2

            if nums[Min] < nums[Mid]:
                Min = Mid

            elif nums[Max] > nums[Mid]:
                Max = Mid

            else:
                return min(nums[Min:Max + 1])


# Rotated sorted array contains one pivot where order breaks.
# Use binary search to identify which half is sorted.
# If left half is sorted → minimum lies in right half.
# If right half is sorted → minimum lies in left half including Mid.
# Final minimum exists near the rotation pivot.