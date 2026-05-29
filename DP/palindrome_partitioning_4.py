"""
Problem: Palindrome Partitioning IV
Platform: LeetCode
Link: https://leetcode.com/problems/palindrome-partitioning-iv/
Approach: Brute Force / Two Cut Partitioning
Time Complexity: O(n^3)
Space Complexity: O(n)
"""

class Solution:

    def checkPartitioning(self, s: str) -> bool:

        def isP(s):

            if s[:] == s[::-1]:
                return True

            else:
                return False

        for i in range(1, len(s) - 1):

            for j in range(i + 1, len(s)):

                if isP(s[:i]) and isP(s[i:j]) and isP(s[j:]):
                    return True

        return False


# Try every possible way to place two cuts in the string.
# These two cuts divide the string into three non-empty parts.
# Check whether all three parts are palindromes.
# isP() checks palindrome by comparing string with its reverse.
# If any valid partition exists → return True.