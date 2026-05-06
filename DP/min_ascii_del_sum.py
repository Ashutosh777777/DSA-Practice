"""
Problem: Minimum ASCII Delete Sum for Two Strings
Platform: LeetCode
Link: https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings/
Approach: Dynamic Programming on Strings
Time Complexity: O(m * n)
Space Complexity: O(m * n)
"""

class Solution(object):
    def minimumDeleteSum(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """

        m = len(s1)
        n = len(s2)

        t = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            t[i][0] = t[i - 1][0] + ord(s1[i - 1])

        for j in range(1, n + 1):
            t[0][j] = t[0][j - 1] + ord(s2[j - 1])

        for i in range(1, m + 1):
            for j in range(1, n + 1):

                if s1[i - 1] == s2[j - 1]:
                    t[i][j] = t[i - 1][j - 1]

                else:
                    del_s1 = t[i - 1][j] + ord(s1[i - 1])
                    del_s2 = t[i][j - 1] + ord(s2[j - 1])

                    t[i][j] = min(del_s1, del_s2)

        return t[m][n]

# DP state: t[i][j] = minimum ASCII delete sum for s1[0:i] and s2[0:j].
# If characters match, no deletion needed → take diagonal value.
# Otherwise, either delete from s1 or delete from s2.
# Initialize first row/column with cumulative ASCII sums.
# Final answer is stored at t[m][n].