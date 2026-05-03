"""
Problem: Minimum Cost to Cut a Stick
Platform: LeetCode
Link: https://leetcode.com/problems/minimum-cost-to-cut-a-stick/
Approach: Memoization (DP) / MCM Pattern
Time Complexity: O(m^3)
Space Complexity: O(m^2)
"""

class Solution(object):
    def minCost(self, n, cuts):
        """
        :type n: int
        :type cuts: List[int]
        :rtype: int
        """

        cuts.sort()
        cuts = [0] + cuts + [n]
        m = len(cuts)

        t = [[-1] * (m + 1) for _ in range(m + 1)]

        def solve(i, j):
            if j - i == 1:
                return 0

            if t[i][j] != -1:
                return t[i][j]

            ans = float('inf')

            for k in range(i + 1, j):
                temp = cuts[j] - cuts[i] + solve(i, k) + solve(k, j)
                ans = min(temp, ans)

            t[i][j] = ans
            return ans

        return solve(0, len(cuts) - 1)

# Add 0 and n to represent boundaries of the stick.
# DP state: t[i][j] = minimum cost to cut stick between cuts[i] and cuts[j].
# Try every possible cut k between i and j.
# Cost = current stick length + left part + right part.
# Use memoization to avoid recomputation of overlapping subproblems.