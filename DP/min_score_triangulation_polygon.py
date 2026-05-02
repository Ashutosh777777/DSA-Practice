"""
Problem: Minimum Score Triangulation of Polygon
Platform: LeetCode
Link: https://leetcode.com/problems/minimum-score-triangulation-of-polygon/
Approach: Matrix Chain Multiplication Pattern + Memoization
Time Complexity: O(n^3)
Space Complexity: O(n^2)
"""

class Solution(object):
    def minScoreTriangulation(self, values):
        """
        :type values: List[int]
        :rtype: int
        """

        n = len(values)
        t = [[-1] * (n + 1) for _ in range(n + 1)]

        def solve(i, j):
            if j - i < 2:
                return 0

            if t[i][j] != -1:
                return t[i][j]

            ans = float('inf')

            for k in range(i + 1, j):
                temp = solve(i, k) + solve(k, j) + values[i] * values[k] * values[j]
                ans = min(temp, ans)

            t[i][j] = ans
            return ans

        return solve(0, n - 1)

# Choose every possible k between i and j to form triangle (i, k, j).
# Cost of one triangle = values[i] * values[k] * values[j].
# Recursively solve left polygon (i to k) and right polygon (k to j).
# Base case: fewer than 3 vertices means no triangle can be formed.