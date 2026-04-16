"""
Problem: Longest Common Substring
Platform: GFG
Link: https://www.geeksforgeeks.org/problems/longest-common-substring1452/1
Approach: Dynamic Programming
Time Complexity: O(n * m)
Space Complexity: O(n * m)
"""
class Solution:
    def longCommSubstr(self, s1, s2):
        # code here
        n = len(s1)
        m = len(s2)
        longest = 0
        t = [[0]*(m+1) for _ in range(n+1)]
        
        for i in range(1, n+1):
            for j in range(1, m+1):
                if s1[i-1] == s2[j-1]:
                    t[i][j] = 1 + t[i-1][j-1]
                    longest = max(longest, t[i][j])
                else:
                    t[i][j] = 0
        return longest
# Define dp[i][j] as length of longest common substring ending at i-1 and j-1.
# If characters match, extend substring: dp[i][j] = 1 + dp[i-1][j-1].
# If not, reset to 0 since substring must be continuous.
# Track maximum value during traversal.