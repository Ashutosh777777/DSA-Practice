"""
Problem: Shortest Common Supersequence
Platform: LeetCode
Link: https://leetcode.com/problems/shortest-common-supersequence/
Approach: LCS + Backtracking
Time Complexity: O(n * m)
Space Complexity: O(n * m)
"""
class Solution(object):
    def shortestCommonSupersequence(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        n = len(str1)
        m = len(str2)

        t = [[0]*(m+1) for _ in range(n+1)]

        for i in range(1, n+1):
            for j in range(1, m+1):
                if str1[i-1] == str2[j-1]:
                    t[i][j] = 1 + t[i-1][j-1]
                else:
                    t[i][j] = max(t[i-1][j], t[i][j-1])

        i, j = n, m
        res = ""

        while i > 0 and j > 0:
            if str1[i-1] == str2[j-1]:
                res = str1[i-1] + res
                i -= 1
                j -= 1
            elif t[i-1][j] > t[i][j-1]:
                res = str1[i-1] + res
                i -= 1
            else:
                res = str2[j-1] + res
                j -= 1

        while i > 0:
            res = str1[i-1] + res
            i -= 1

        while j > 0:
            res = str2[j-1] + res
            j -= 1

        return res
# First compute LCS DP table.
# Traverse from bottom-right to build result string.
# If characters match → include once and move diagonally.
# If not → include character from direction of larger DP value.