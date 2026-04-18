"""
Problem: Minimum Insertions to Make a String Palindrome
Platform: LeetCode
Link: https://leetcode.com/problems/minimum-insertion-steps-to-make-a-string-palindrome/
Approach: LCS(s, reverse(s)) → Longest Palindromic Subsequence
Time Complexity: O(n^2)
Space Complexity: O(n^2)
"""
class Solution(object):
    def minInsertions(self, s):
        """
        :type s: str
        :rtype: int
        """
        p = s[::-1]

        n = len(s)
        t = [[0]*(n+1) for _ in range(n+1)]

        for i in range(1,n+1):
            for j in range(1, n+1):
                if s[i-1]==p[j-1]:
                    t[i][j] = 1 + t[i-1][j-1]
                else:
                    t[i][j] = max(t[i-1][j], t[i][j-1])
        return n - t[n][n]
# Compute LPS using LCS between string and its reverse.
# LPS gives longest part already forming a palindrome.
# Remaining characters must be inserted to balance the string.
# Minimum insertions = n − LPS.