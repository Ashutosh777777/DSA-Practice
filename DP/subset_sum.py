"""
Problem: Subset Sum Problem
Platform: GFG
Link: https://www.geeksforgeeks.org/problems/subset-sum-problem-1611555638/1
Approach: Dynamic Programming (0/1 Knapsack pattern)
Time Complexity: O(n * target)
Space Complexity: O(n * target)
"""
class Solution:
    def isSubsetSum (self, arr, target):
        # code here     
        n = len(arr)
    
        dp = [[False]*(target+1) for _ in range(n+1)]
        for i in range(n+1):

            dp[i][0] = True
        
        for i in range(1, n+1):
            for j in range(1, target+1):
                if arr[i-1] <= j:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-arr[i-1]]
                else:
                    dp[i][j] = dp[i-1][j]
        
        return dp[n][target]
            
# Define dp[i][j] as whether a subset of first i elements can form sum j.
# Initialize dp[i][0] = True since sum 0 is always possible (empty subset).
# For each element, either include it or exclude it based on feasibility.
# Final answer is dp[n][target].