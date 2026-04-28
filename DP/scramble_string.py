"""
Problem: Scramble String
Platform: LeetCode
Link: https://leetcode.com/problems/scramble-string/
Approach: Recursion + Memoization (DP)
Time Complexity: Exponential (optimized with memoization)
Space Complexity: O(n^2) + recursion stack
"""

class Solution(object):
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        memo = {}

        def solve(s1, s2):
            if s1 == s2:
                return True

            if len(s1) <= 1:
                return False

            key = (s1, s2)
            if key in memo:
                return memo[key]

            n = len(s1)
            flag = False

            for i in range(1, n):
                if (solve(s1[:i], s2[n-i:]) and solve(s1[i:], s2[:n-i])) or \
                   (solve(s1[:i], s2[:i]) and solve(s1[i:], s2[i:])):
                    flag = True
                    break

            memo[key] = flag
            return flag

        return solve(s1, s2)

# Try every partition index and check both swapped and non-swapped cases.
# If both left and right parts match recursively, strings are scramble strings.
# Use memoization with (s1, s2) pair to avoid repeated substring checks.
# Base case: if both strings are same → True, if length <= 1 → False.