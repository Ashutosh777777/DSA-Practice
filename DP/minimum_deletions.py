"""
Problem: Minimum Deletions to Make a String Palindrome
Platform: GFG
Link: https://www.geeksforgeeks.org/problems/minimum-deletions/1
Approach: LCS(s, reverse(s)) → Longest Palindromic Subsequence
Time Complexity: O(n^2)
Space Complexity: O(n^2)
"""
class Solution:
    def minDeletions(self,s):
        # code here 
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
        return n - t[n][m]
# Compute LPS using LCS(s, reverse(s)).
# LPS gives maximum characters that can stay in palindrome.
# Delete remaining characters.
# Minimum deletions = n − LPS.