"""
Problem: Minimum Operations to Make Array Non-Decreasing
Platform: LeetCode
Link: Weekly Contest 499 - Q3
Approach: Greedy using Sum of Positive Drops
Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0

        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                ans += nums[i] - nums[i + 1]

        return ans


# Whenever nums[i] > nums[i+1], the right side must be increased.
# Required increase is exactly nums[i] - nums[i+1].
# Since one subarray increment operation costs only x, we sum all positive drops.
# Final answer is the total of all adjacent decreases in the array.