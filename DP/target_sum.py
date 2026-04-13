"""
Problem: Target Sum
Platform: LeetCode
Link: https://leetcode.com/problems/target-sum/
Approach: DP (transform to subset sum count)
Time Complexity: O(n * target)
Space Complexity: O(n * target)
"""
class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        diff = target
        arr = nums[:]
        if (sum(arr)+diff)%2!=0:
            return 0
        target = (sum(arr)+diff)//2
        total = sum(arr)
        if sum(arr) < abs(diff):
            return 0
        n = len(arr)
        t = [[0]*(target+1) for _ in range(n+1)]
        for i in range(n+1):
            t[i][0] = 1
            
        for i in range(1, n+1):
            for j in range(target+1):
                if arr[i-1] <= j:
                    t[i][j] = t[i-1][j] + t[i-1][j-arr[i-1]]
                else:
                    t[i][j] = t[i-1][j]
        return t[n][target]
# Convert +/− assignment into subset sum: find subsets with sum = (total + target) / 2.
# If (total + target) is odd or total < |target|, return 0.
# Use DP where dp[i][j] counts ways to form sum j using first i elements.
# Return number of ways to form the transformed target sum.