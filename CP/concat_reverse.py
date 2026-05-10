"""
Problem: Concatenation with Reverse
Platform: LeetCode
Link: 
Approach: Array Slicing
Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution(object):
    def concatWithReverse(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        return nums[::] + nums[::-1]


# nums[::] creates a copy of the original array.
# nums[::-1] creates the reversed version of the array.
# Concatenate both arrays using + operator.
# Final array contains original elements followed by reversed elements.