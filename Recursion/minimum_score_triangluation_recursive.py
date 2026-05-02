"""
Problem: Minimum Score Triangulation of Polygon
Platform: LeetCode
Link: https://leetcode.com/problems/minimum-score-triangulation-of-polygon/
Approach: Pure Recursion / MCM Pattern
Time Complexity: Exponential
Space Complexity: O(n) recursion stack
"""

class Solution(object):
    def minScoreTriangulation(self, values):
        """
        :type values: List[int]
        :rtype: int
        """

        def solve(i, j):
            if j - i < 2:
                return 0

            ans = float('inf')

            for k in range(i + 1, j):
                cost = values[i] * values[k] * values[j] + solve(i, k) + solve(k, j)
                ans = min(ans, cost)

            return ans

        return solve(0, len(values) - 1)

# Choose every possible k between i and j to form triangle (i, k, j).
# Cost = current triangle cost + left polygon cost + right polygon cost.
# Base case: fewer than 3 vertices means no triangle can be formed.
# No memoization, so same subproblems are recalculated many times.