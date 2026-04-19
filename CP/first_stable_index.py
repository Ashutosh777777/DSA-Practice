"""
Problem: First Stable Index
Platform: LeetCode
Approach: Brute Force (prefix max + suffix min per index)
Time Complexity: O(n^2)
Space Complexity: O(1)
"""
class Solution(object):
    def firstStableIndex(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        for i in range(n):
            val = (max(nums[:i+1]) - min(nums[i:]))
            if val<=k:
                return i
        return -1
# For each index i, compute max of prefix nums[0..i].
# Compute min of suffix nums[i..n-1].
# Calculate instability = prefix max − suffix min.
# Return first index where instability ≤ k, else -1.