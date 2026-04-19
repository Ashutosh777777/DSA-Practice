"""
Problem: First Stable Index
Platform: LeetCode
Approach: Prefix maximum + suffix minimum precomputation
Time Complexity: O(n)
Space Complexity: O(n)
"""
class Solution(object):
    def firstStableIndex(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums) 
        p = [0]*n
        s = [0]*n

        p[0] = nums[0]
        for i in range(1, n):
            p[i] = max(p[i-1], nums[i])
        s[-1] = nums[-1]
        for i in range(n-2, -1, -1):
            s[i] = min(s[i+1], nums[i])
        for i in range(n):
            if p[i] - s[i]<=k:
                return i
        return -1
        
# Precompute p[i] as maximum element from nums[0..i].
# Precompute s[i] as minimum element from nums[i..n-1].
# For each index, compute instability as p[i] - s[i].
# Return the first index where instability ≤ k, otherwise return -1.