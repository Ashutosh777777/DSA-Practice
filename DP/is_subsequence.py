"""
Problem: Is Subsequence
Platform: LeetCode
Link: https://leetcode.com/problems/is-subsequence/
Approach: LCS-based check
Time Complexity: O(n * m)
Space Complexity: O(n * m)
"""
class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        n = len(s)
        m = len(t)

        dp = [[0]*(m+1) for _ in range(n+1)]

        for i in range(1, n+1):
            for j in range(1, m+1):
                if s[i-1]==t[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return len(s)==dp[n][m]
# Compute LCS of s and t.
# If s is a subsequence of t, then LCS length must equal len(s).
# Use standard LCS DP with include/exclude transitions.
# Return whether full length of s is matched.