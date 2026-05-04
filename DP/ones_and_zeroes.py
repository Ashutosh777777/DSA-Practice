"""
Problem: Ones and Zeroes
Platform: LeetCode
Link: https://leetcode.com/problems/ones-and-zeroes/
Approach: 0/1 Knapsack with 3D DP
Time Complexity: O(l * m * n)
Space Complexity: O(l * m * n)
"""

class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """

        l = len(strs)

        t = [[[0 for _ in range(n + 1)] for _ in range(m + 1)] for _ in range(l + 1)]

        for i in range(1, l + 1):
            zero = strs[i - 1].count("0")
            one = strs[i - 1].count("1")

            for j in range(m + 1):
                for k in range(n + 1):
                    if zero <= j and one <= k:
                        t[i][j][k] = max(
                            1 + t[i - 1][j - zero][k - one],
                            t[i - 1][j][k]
                        )
                    else:
                        t[i][j][k] = t[i - 1][j][k]

        return t[l][m][n]

# Treat each string as an item in 0/1 knapsack.
# Each string has two weights: number of 0s and number of 1s.
# DP state: t[i][j][k] = max strings using first i strings, j zeroes, k ones.
# For each string, either include it or exclude it.