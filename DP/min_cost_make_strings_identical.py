"""
Problem: Minimum Cost to Make Two Strings Identical
Platform: GFG
Link: https://www.geeksforgeeks.org/problems/minimum-cost-to-make-two-strings-identical1107/1
Approach: DP on Strings (Deletion Cost Based)
Time Complexity: O(m * n)
Space Complexity: O(m * n)
"""

# User function Template for python3

class Solution:
    def findMinCost(self, x, y, costX, costY):

        m = len(x)
        n = len(y)

        t = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            t[i][0] = t[i - 1][0] + costX

        for j in range(1, n + 1):
            t[0][j] = t[0][j - 1] + costY

        for i in range(1, m + 1):
            for j in range(1, n + 1):

                if x[i - 1] == y[j - 1]:
                    t[i][j] = t[i - 1][j - 1]

                else:
                    del_x = t[i - 1][j] + costX
                    del_y = t[i][j - 1] + costY

                    t[i][j] = min(del_x, del_y)

        return t[m][n]

# DP state: t[i][j] = minimum cost to make x[0:i] and y[0:j] identical.
# If characters match, no deletion cost is needed.
# Otherwise, either delete character from x or from y.
# First row/column represent deleting all characters from one string.
# Final answer is stored at t[m][n].