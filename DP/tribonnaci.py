"""
Problem: N-th Tribonacci Number
Platform: LeetCode
Link: https://leetcode.com/problems/n-th-tribonacci-number/
Approach: Recursion + Memoization (DP)
Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """

        t = [-1] * (n + 1)

        def solve(n):
            if n == 0:
                return 0
            if n == 1 or n == 2:
                return 1

            if t[n] != -1:
                return t[n]

            t[n] = solve(n - 1) + solve(n - 2) + solve(n - 3)
            return t[n]

        return solve(n)

# Each value depends on previous three values: T(n) = T(n-1) + T(n-2) + T(n-3).
# Base cases handle first three values directly.
# Use memoization array to avoid recomputing subproblems.
# Important: store result in DP and return it (avoid recomputing again).