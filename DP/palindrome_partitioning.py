"""
Problem: Palindrome Partitioning
Platform: GeeksforGeeks
Approach: Precompute palindromes, then use DP to find minimum cuts
Time Complexity: O(n²)
Space Complexity: O(n²)
"""

class Solution:
    def palPartition(self, s):
        n = len(s)

        pal = [[False] * n for _ in range(n)]

        for gap in range(n):
            for i in range(n - gap):
                j = i + gap

                if s[i] == s[j]:
                    if gap <= 1:
                        pal[i][j] = True
                    else:
                        pal[i][j] = pal[i + 1][j - 1]

        dp = [0] * n

        for i in range(n):
            if pal[0][i]:
                dp[i] = 0
            else:
                mini = float('inf')

                for j in range(i):
                    if pal[j + 1][i]:
                        mini = min(mini, dp[j] + 1)

                dp[i] = mini

        return dp[n - 1]


# pal[i][j] stores whether substring s[i:j+1] is a palindrome.
# dp[i] stores the minimum cuts needed for substring s[0:i+1].
# If s[0:i+1] is already a palindrome, no cut is needed.
# Otherwise, try every previous cut position and take the minimum valid answer.