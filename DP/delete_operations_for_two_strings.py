"""
Problem: Delete Operation for Two Strings
Platform: LeetCode
Link: https://leetcode.com/problems/delete-operation-for-two-strings/
Approach: LCS-based
Time Complexity: O(n * m)
Space Complexity: O(n * m)
"""
class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        n = len(word1)
        m = len(word2)
        t = [[0]*(m+1) for _ in range(n+1)]

        for i in range(1, n+1):
            for j in range(1, m+1):
                if word1[i-1]==word2[j-1]:
                    t[i][j] = 1+ t[i-1][j-1]
                else:
                    t[i][j] = max(t[i-1][j], t[i][j-1])
        return (m+n)-2*(t[n][m])
# Find LCS of both strings.
# LCS represents characters we keep (no deletion needed).
# Delete remaining characters from both strings.
# Total deletions = (n − LCS) + (m − LCS).