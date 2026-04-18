"""
Problem: Minimum Insertions to Form a Palindrome
Platform: GFG
Link: https://www.geeksforgeeks.org/problems/form-a-palindrome1455/1
Approach: LCS(s, reverse(s)) → Longest Palindromic Subsequence
Time Complexity: O(n^2)
Space Complexity: O(n^2)
"""
class Solution:
    def findMinInsertions(self, s):
        # code here
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
# Reverse the string and compute LCS with original string.
# LCS gives the Longest Palindromic Subsequence (LPS).
# Characters not in LPS need to be inserted to form palindrome.
# Minimum insertions = n - LPS.