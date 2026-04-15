"""
Problem: Longest Common Subsequence (LCS)
Platform: LeetCode
Link: https://leetcode.com/problems/longest-common-subsequence/
Approach: Recursion (brute force)
Time Complexity: O(2^(n+m)) exponential
Space Complexity: O(n + m) recursion stack
"""
class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        def rec(a, b):
            if not a or not b:
                return 0
            l1 = len(a)
            l2 = len(b)
            if a[l1-1]==b[l2-1]:
                return 1 + rec(a[:l1-1], b[:l2-1])
            else:
                return max(rec(a[:], b[:l2-1]), rec(a[:l1-1], b[:]))
        return rec(text1, text2)
# Compare last characters of both strings.
# If they match, include it and recurse on remaining substrings.
# If not, recurse by excluding one character from either string and take max.
# Base case: if any string becomes empty, return 0.