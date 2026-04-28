"""
Problem: Unique Paths
Platform: LeetCode
Link: https://leetcode.com/problems/unique-paths/
Approach: Recursion + Memoization (DP)
Time Complexity: O(m * n)
Space Complexity: O(m * n)
"""

class Solution(object):
    def uniquePaths(self, m, n):
        t = [[-1] * n for _ in range(m)]

        def solve(i, j):
            if i == m - 1 and j == n - 1:
                return 1

            if i >= m or j >= n:
                return 0

            if t[i][j] != -1:
                return t[i][j]

            t[i][j] = solve(i + 1, j) + solve(i, j + 1)
            return t[i][j]

        return solve(0, 0)

# From each cell, we can move only right or down.
# If destination cell is reached, count it as 1 valid path.
# If indices go out of bounds, return 0 since path is invalid.
# Use memoization to store paths from each cell and avoid recomputation.