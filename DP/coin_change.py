"""
Problem: Coin Change (Minimum Coins)
Platform: LeetCode
Link: https://leetcode.com/problems/coin-change/
Approach: Dynamic Programming (Unbounded Knapsack - Min)
Time Complexity: O(n * amount)
Space Complexity: O(n * amount)
"""
class Solution(object):
    def coinChange(self, coins, amount):
        n = len(coins)
        
        t = [[float('inf')] * (amount + 1) for _ in range(n + 1)]
        
        for i in range(n + 1):
            t[i][0] = 0
        
        for i in range(1, n + 1):
            for j in range(1, amount + 1):
                if coins[i-1] <= j:
                    t[i][j] = min(1 + t[i][j - coins[i-1]], t[i-1][j])
                else:
                    t[i][j] = t[i-1][j]
        
        return t[n][amount] if t[n][amount] != float('inf') else -1
# Define dp[i][j] as minimum coins needed to make sum j using first i coins.
# Initialize with infinity, and dp[i][0] = 0 since 0 coins needed for sum 0.
# Either take the coin (reuse allowed) or skip it.
# Return minimum coins or -1 if impossible.