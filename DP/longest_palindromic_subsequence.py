"""
Problem: Longest Palindromic Subsequence
Platform: LeetCode
Link: https://leetcode.com/problems/longest-palindromic-subsequence/
Approach: LCS(s, reverse(s))
Time Complexity: O(n^2)
Space Complexity: O(n^2)
"""
class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        p = s[::-1]
        n = len(s)
        m = len(p)

        t = [[0]*(m+1) for _ in range(n+1)]
        for i in range(1, n+1):
            for j in range(1, m+1):
                if s[i-1]==p[j-1]:
                    t[i][j] = 1 + t[i-1][j-1]
                else:
                    t[i][j] = max(t[i-1][j], t[i][j-1])
        return t[n][m]
# Reverse the string and find LCS of original and reversed string.
# LCS will be the longest palindromic subsequence.
# DP state: dp[i][j] = LCS length of s[0..i-1] and rev[0..j-1].
# Final answer = dp[n][n].