"""
Problem: Min Cost Climbing Stairs
Platform: LeetCode
Link: https://leetcode.com/problems/min-cost-climbing-stairs/
Approach: Recursion + Memoization (DP)
Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """

        memo = {}

        def solve(i):
            if i >= len(cost):
                return 0

            if i in memo:
                return memo[i]

            memo[i] = cost[i] + min(solve(i + 1), solve(i + 2))
            return memo[i]

        return min(solve(0), solve(1))

# From each stair, we can move either 1 step or 2 steps ahead.
# Cost of current stair is added, then choose minimum of next two paths.
# Use memoization to avoid recalculating same index multiple times.
# Final answer is min(starting from index 0, starting from index 1).