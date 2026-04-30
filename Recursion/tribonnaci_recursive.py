"""
Problem: N-th Tribonacci Number
Platform: LeetCode
Link: https://leetcode.com/problems/n-th-tribonacci-number/
Approach: Pure Recursion (Brute Force)
Time Complexity: Exponential (~O(3^n))
Space Complexity: O(n) recursion stack
"""

class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """

        def solve(n):
            if n == 0:
                return 0
            if n == 1 or n == 2:
                return 1

            return solve(n - 1) + solve(n - 2) + solve(n - 3)

        return solve(n)

# Each value depends on sum of previous three values.
# Recomputes same subproblems multiple times → very inefficient.
# No memoization → exponential time.
# Useful for understanding recurrence before applying DP.