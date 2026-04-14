"""
Problem: Coin Change II
Platform: LeetCode
Link: https://leetcode.com/problems/coin-change-ii/
Approach: DP (Unbounded Knapsack - Count Ways)
Time Complexity: O(n * amount)
Space Complexity: O(n * amount)
"""
class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        n = len(coins)
        t = [[0]*(amount+1) for _ in range(n+1)]
        for i in range(n+1):
            t[i][0] = 1
        for i in range(1, n+1):
            for j in range(amount+1):
                if coins[i-1] <= j:
                    t[i][j] = t[i][j-coins[i-1]] + t[i-1][j]
                else:
                    t[i][j] = t[i-1][j]
        return t[n][amount]
# Define dp[i][j] as number of ways to form sum j using first i coins.
# Initialize dp[i][0] = 1 since there’s one way to make sum 0.
# Either include coin (reuse allowed) or exclude it.
# Add both possibilities to count total ways.