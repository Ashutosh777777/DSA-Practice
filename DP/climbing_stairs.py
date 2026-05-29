"""
Problem: Climbing Stairs
Platform: LeetCode
Link: https://leetcode.com/problems/climbing-stairs/
Approach: Dynamic Programming
Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution(object):

    def climbStairs(self, n):

        if n == 0:
            return 0

        if n == 1:
            return 1

        if n == 2:
            return 2

        dp = [0] * (n + 1)

        dp[1] = 1
        dp[2] = 2

        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]


# To reach step i, we can come from step i-1 or step i-2.
# Therefore, dp[i] = dp[i-1] + dp[i-2].
# dp[1] = 1 and dp[2] = 2 are base cases.
# Fill the dp array from smaller steps to larger steps.
# Final answer is stored in dp[n].