"""
Problem: Partition Equal Subset Sum
Platform: LeetCode
Link: https://leetcode.com/problems/partition-equal-subset-sum/
Approach: Dynamic Programming (subset sum transformation)
Time Complexity: O(n * target)
Space Complexity: O(n * target)
"""
class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        s = sum(nums)
        if s%2!=0:
            return False
        target = s//2
        n = len(nums)

        t = [[False]*(target+1) for _ in range(n+1)]
        for i in range(n+1):
            t[i][0] = True
        
        for i in range(1, n+1):
            for j in range(1, target+1):
                if nums[i-1]<=j:
                    t[i][j] = t[i-1][j] or t[i-1][j-nums[i-1]]
                else:
                    t[i][j] = t[i-1][j]
        return t[n][target]
# Compute total sum; if it’s odd, partition is impossible.
# Convert problem to finding a subset with sum = total_sum / 2.
# Use DP where dp[i][j] tells if sum j can be formed using first i elements.
# Return whether target sum is achievable.