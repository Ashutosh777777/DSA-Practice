"""
Problem: Minimum Cost to Cut a Stick
Platform: LeetCode
Link: https://leetcode.com/problems/minimum-cost-to-cut-a-stick/
Approach: Pure Recursion / MCM Pattern
Time Complexity: Exponential
Space Complexity: O(c) recursion stack
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

        def solve(i, j):
            if j - i == 1:
                return 0

            ans = float('inf')

            for k in range(i + 1, j):
                temp = cuts[j] - cuts[i] + solve(i, k) + solve(k, j)
                ans = min(temp, ans)

            return ans

        return solve(0, len(cuts) - 1)

# Add 0 and n to represent both ends of the stick.
# Choose every possible cut k between i and j.
# Cost of cutting current stick = cuts[j] - cuts[i].
# Recursively solve left and right parts after making the cut.
# No memoization, so same subproblems are recalculated many times.