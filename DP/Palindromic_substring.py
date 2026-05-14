"""
Problem: Palindromic Substrings
Platform: LeetCode
Link: https://leetcode.com/problems/palindromic-substrings/
Approach: Recursion + Memoization (Palindrome DP)
Time Complexity: O(n^2)
Space Complexity: O(n^2)
"""

class Solution(object):

    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """

        count = 0
        t = {}
        n = len(s)

        def solve(i, j):

            if i >= j:
                return True

            if (i, j) in t:
                return t[(i, j)]

            if s[i] == s[j] and solve(i + 1, j - 1):
                t[(i, j)] = True

            else:
                t[(i, j)] = False

            return t[(i, j)]

        for i in range(n):

            for j in range(i, n):

                if solve(i, j):
                    count += 1

        return count


# Check every substring using recursion and memoization.
# A substring is palindrome if end characters match
# and inner substring is also palindrome.
# Base case: single character or empty substring is palindrome.
# Memoization avoids recalculating overlapping subproblems.
# Count all substrings that satisfy palindrome condition.